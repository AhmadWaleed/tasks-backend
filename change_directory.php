<?php

declare(strict_types=1);

class Path
{
    public function __construct(public string $currentPath)
    {
        static::assertValidPath($this->currentPath);
    }

    public function cd(string $path): self
    {
        if ($path === DIRECTORY_SEPARATOR) {
            return new self('/');
        }

        $segments = explode(DIRECTORY_SEPARATOR, $path);
        $sub = implode(
            DIRECTORY_SEPARATOR,
            array_filter($segments, fn(string $item) => !empty($item) && $item !== '..' && $item !== '.')
        );

        $counts = array_count_values($segments);

        if (isset($counts['..'])) {
            $parent = $this->getParentPath($counts['..']);
            if ($parent === DIRECTORY_SEPARATOR) {
                return new self($parent . $sub);
            }

            return new self($parent . DIRECTORY_SEPARATOR . $sub);
        }

        return new self($this->currentPath . DIRECTORY_SEPARATOR . $sub);
    }

    private function getParentPath(int $depth): string
    {
        $loop = $depth;
        $path = $this->currentPath;

        while ($loop) {
            $loop--;

            if (strlen($path) === 2) {
                return DIRECTORY_SEPARATOR;
            }

            if ($pos = strrpos($path, DIRECTORY_SEPARATOR)) {
                $path = substr($path, 0, $pos);
            }
        }

        return $path;
    }

    private static function assertValidPath(string $path): void
    {
        if (!preg_match("/^[a-zA-Z\/\d]+$/", $path)) {
            throw new InvalidArgumentException(
                "Invalid path: directory names consist only of English alphabet letters (A-Z and a-z)"
            );
        }
    }
}

/**
 * This solution uses php 8.0, and provide implementation of
 * an abstract file system using Immutable Path::class, please
 * see examples below for solution.
 */

$path = new Path('/a/b/c/d');
$pathOneLevelIn = $path->cd('/x');
var_dump($pathOneLevelIn->currentPath);
$pathOneLevelUp = $path->cd('../x');
var_dump($pathOneLevelUp->currentPath);
$pathTowLevelUp = $path->cd('../../x');
var_dump($pathTowLevelUp->currentPath);
$edgeCaseOne = $path->cd('./x');
var_dump($edgeCaseOne->currentPath);
$edgeCaseTwo = $path->cd('../../../../x');
var_dump($edgeCaseTwo->currentPath);
$root = $path->cd('/');
var_dump($root->currentPath);
