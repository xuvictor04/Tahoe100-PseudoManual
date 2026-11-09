---
symbol: "ASCL1"
type: "gene"
col: 6297
ensembl_id: "ENSG00000139352"
name: "achaete-scute family bHLH transcription factor 1"
location: "12q23.2"
module: 9
arm: "+"
pooled_cpm: 4.32
n_lines_expressing: 9
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 25
direction_downstream: 57
tags: ["gene", "module/009", "written"]
generated_by: "tahoemap"
---

# ASCL1

*achaete-scute family bHLH transcription factor 1* — 12q23.2

> [!summary] In one line
> ASCL1 is a basic helix-loop-helix transcription factor that drives neuronal and neuroendocrine lineage commitment, and acts as a lineage-dependency oncogene in small-cell lung cancer.

## What it is

ASCL1 (Mash1) heterodimerises with E-proteins and binds E-boxes, and is one of the proneural factors: mice lacking it fail to make olfactory and autonomic neurons, and ASCL1 is the indispensable member of the three-factor cocktail that converts fibroblasts directly into neurons. Notch-HES signalling and rapid turnover keep it pulsatile in progenitors, and it must be extinguished for differentiation to finish. In cancer it defines a lineage state rather than a mutation: ASCL1-high small-cell lung cancer, the SCLC-A subtype, depends on it for survival, and its enhancer programme is distinct from the NEUROD1-driven alternative.

## What is uncertain

ASCL1 shares the E-box consensus with the other bHLH factors, so an activity inferred from its targets may be reporting generic E-box occupancy, or the neuroendocrine lines in the panel, rather than ASCL1. The well-supported part of this gene's biology — proneural specification and SCLC lineage dependency — is largely orthogonal to a 24 h drug-response readout in pooled cancer lines.

## References

- Guillemot et al., 1993, Cell — Mash1-null mice lack olfactory and autonomic neurons.
- Vierbuchen et al., 2010, Nature — Ascl1 with Brn2 and Myt1l converts fibroblasts into functional neurons.
- Augustyn et al., 2014, PNAS — ASCL1 is a lineage-specific oncogene required for survival of ASCL1-high small-cell lung cancer.
- Borromeo et al., 2016, Cell Reports — ASCL1 and NEUROD1 bind distinct enhancer programmes defining SCLC subtypes.
- Rudin et al., 2019, Nature Reviews Cancer — synthesis defining SCLC subtypes, with SCLC-A keyed to ASCL1.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.34× (z +6.2, q 3e-07, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.79× (z +3.6, q 0.037, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0155×; ⚠ cell-cycle shift, explains ~87% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0214×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0702×; ⚠ cell-cycle shift, explains ~37% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0429×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.0669×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.159×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIT2]] (+0.98, fdr 7e-06), [[SYT4]] (+0.97, fdr 7e-06), [[SRRM4]] (+0.95, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 57 go from it, the strongest it → [[RALYL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +6.2 | 3e-07 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +5.3 | 3e-05 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +3.9 | 0.017 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.40×** | +3.8 | 0.017 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.037 | 1/3 (SK-MEL-2) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.62×** | +3.5 | 0.042 | 0/1 | inconsistent across doses | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.49×** | +3.4 | 0.057 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.72×** | +3.4 | 0.057 | 0/1 | top dose only | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 2.05× | +3.1 | 0.13 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 2.06× | +3.0 | 0.13 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0155×; ⚠ cell-cycle shift, explains ~87% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0214×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0702×; ⚠ cell-cycle shift, explains ~37% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0429×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.0669×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.500× | -3.0 | 0.84 | 2/3 (SHP-77, LOX-IMVI) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 214 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0155× (z -19.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0429× (z -14.5) |
| [[A-172 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.506 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIT2]] | +0.98 | +0.98 / +0.98 | both halves | 7e-06 | pathway: Signaling by NTRK1 (TRKA) |
| [[SYT4]] | +0.97 | +0.98 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.95 | +0.89 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.93 | +0.94 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.89 | +0.91 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.83 | +0.89 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[PCSK1]] | +0.81 | +0.81 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[CGA]] | +0.81 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SNTG1]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises ASCL1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.81× lower at baseline in the lines without CALCA | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises ASCL1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.11× lower at baseline in the lines without SYT4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises ASCL1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.32× lower at baseline in the lines without RIT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises ASCL1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.55× lower at baseline in the lines without KCNB2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises ASCL1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.07× lower at baseline in the lines without SRRM4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises ASCL1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without AK4P3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises ASCL1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without NAA11 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises ASCL1's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 2.92× lower at baseline in the lines without LINC01456 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[CGA]] | C | CGA activity raises ASCL1's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.29× lower at baseline in the lines without CGA | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[H19]] | C | H19 activity raises ASCL1's level | lines that do not express H19 (38) vs lines expressing it (12) | 1.95× lower at baseline in the lines without H19 | 0.033 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises ASCL1's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 2.51× lower at baseline in the lines without GTSF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[HGF]] | C | HGF activity raises ASCL1's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.32× lower at baseline in the lines without HGF | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 15, C 42. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | ASCL1 activity raises RALYL's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.35× lower at baseline in the lines without ASCL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[NRXN1]] | B | ASCL1 activity raises NRXN1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.22× lower at baseline in the lines without ASCL1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[COL21A1]] | B | ASCL1 activity raises COL21A1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without ASCL1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[LINC02306]] | B | ASCL1 activity raises LINC02306's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.67× lower at baseline in the lines without ASCL1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[MYT1L]] | B | ASCL1 activity raises MYT1L's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.35× lower at baseline in the lines without ASCL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[VENTXP1]] | B | ASCL1 activity raises VENTXP1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.74× lower at baseline in the lines without ASCL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[SEMA6D]] | B | ASCL1 activity raises SEMA6D's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.69× lower at baseline in the lines without ASCL1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[CHRM5]] | B | ASCL1 activity raises CHRM5's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.88× lower at baseline in the lines without ASCL1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[GLRA3]] | B | ASCL1 activity raises GLRA3's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.93× lower at baseline in the lines without ASCL1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[UNC80]] | B | ASCL1 activity raises UNC80's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.47× lower at baseline in the lines without ASCL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[XIRP2]] | B | ASCL1 activity raises XIRP2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.33× lower at baseline in the lines without ASCL1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[MIAT]] | B | ASCL1 activity raises MIAT's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.55× lower at baseline in the lines without ASCL1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.7, 37.1); signed map (44.9, 34.2). **Vector** length 25.1, 15.4% of its response variance represented; |z| ≥ 3 in 96 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.55 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +1.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +0.2 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -3.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | achaete-scute family bHLH transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:102,957,674-102,960,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASH1, HASH1, bHLHa46 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Achaete-scute family bHLH transcription factors |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [P50553](https://www.uniprot.org/uniprotkb/P50553) (Achaete-scute homolog 1):

> Transcription factor that plays a key role in neuronal differentiation: acts as a pioneer transcription factor, accessing closed chromatin to allow other factors to bind and activate neural pathways. Directly binds the E box motif (5'-CANNTG-3') on promoters and promotes transcription of neuronal genes. The combination of three transcription factors, ASCL1, POU3F2/BRN2 and MYT1L, is sufficient to reprogram fibroblasts and other somatic cells into induced neuronal (iN) cells in vitro. Plays a …

**Summary**, from NCBI Gene [429](https://www.ncbi.nlm.nih.gov/gene/429):

> This gene encodes a member of the basic helix-loop-helix (BHLH) family of transcription factors. The protein activates transcription by binding to the E box (5'-CANNTG-3'). Dimerization with other BHLH proteins is required for efficient DNA binding. This protein plays a role in the neuronal commitment and differentiation and in the generation of olfactory and autonomic neurons. Mutations in this gene may contribute to the congenital central hypoventilation syndrome (CCHS) phenotype in rare …

**Accessions** — [HGNC:738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:738) · Entrez [429](https://www.ncbi.nlm.nih.gov/gene/429) · UniProt [P50553](https://www.uniprot.org/uniprotkb/P50553) · Ensembl [ENSG00000139352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139352)

## Data

Gene col 6297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6297); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6297]; `tensor/DDL_lfc|DDL_z.npy` [6297]; `embed/gene_vectors.npy` [6297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6297 or target_col == 6297). Every well: [[ASCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ASCL1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
