---
symbol: "PGM5P2"
type: "gene"
col: 15899
ensembl_id: "ENSG00000277778"
name: "phosphoglucomutase 5 pseudogene 2"
location: "9p11.2"
module: 202
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 41
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# PGM5P2

*phosphoglucomutase 5 pseudogene 2* — 9p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +7.9, q 1e-12, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +6.8, q 3e-09, up in 9 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.491× (z -6.3, q 2e-07, down in 18 of 31 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0679×; ⚠ cell-cycle shift, explains ~62% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.0765×; ⚠ cell-cycle shift, explains ~50% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0819×; ⚠ toxic).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGM5P2-1]] (+0.76, fdr 7e-06, ⚠ same locus), [[GPR176]] (+0.59, fdr 1e-05), [[RRAS2]] (+0.51, fdr 7e-05), [[RGS20]] (+0.47, fdr 5e-05); moves opposite to [[SLC45A4]] (-0.43, fdr 1e-04), [[UBR1]] (-0.40, fdr 1e-04), [[DPM2]] (-0.40, fdr 2e-04).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CCBE1]] → it (grade B ⚠); 6 go from it, the strongest it → [[GPR176]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.9 | 1e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +6.8 | 3e-09 | 9/26 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.93×** | +5.8 | 1e-06 | 8/24 (A-172, SW 900, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.1 | 4e-05 | 3/24 (hTERT-HPNE, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.49×** | +5.0 | 8e-05 | 9/31 (A-172, A498, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.5 | 6e-04 | 1/4 (A549) | rises with dose | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +4.4 | 0.001 | 2/14 (LOX-IMVI, CFPAC-1) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.3 | 0.001 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.60×** | +4.1 | 0.002 | 7/32 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.003 | 11/29 (Hs 766T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.8 | 0.008 | 5/20 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.008 | 6/25 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.7 | 0.008 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.008 | 2/20 (NCI-H460, SW480) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.2 | 0.048 | 0/22 | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.054 | 7/27 (A-172, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.060 | 3/33 (HS-578T, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.069 | 3/27 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15899.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0679×; ⚠ cell-cycle shift, explains ~62% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.0765×; ⚠ cell-cycle shift, explains ~50% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0819×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.491×** | -6.3 | 2e-07 | 18/31 (A549, NCI-H2347, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.560×** | -5.1 | 8e-05 | 17/33 (NCI-H2347, HEC-1-A, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -4.9 | 2e-04 | 13/34 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.665×** | -3.6 | 0.043 | 12/30 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.705× | -3.1 | 0.22 | 12/29 (HEC-1-A, AsPC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 4.49 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0765× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LOX-IMVI (line)]] | wt | 5.46 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0679× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.728 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.628 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.677 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.907 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM5P2-1]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GPR176]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[RRAS2]] | +0.51 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[RGS20]] | +0.47 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ZDHHC2]] | +0.47 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[HDAC2-AS2]] | +0.46 | +0.18 / +0.51 | ⚠ one half (not replicated) | 9e-04 |  |
| [[STARD13-AS]] | +0.46 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[SAMD4A]] | +0.45 | +0.29 / +0.38 | both halves | 2e-04 |  |
| [[TRPC4]] | +0.45 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[ARHGEF28]] | +0.44 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[FRMD6-AS2]] | +0.44 | +0.33 / +0.36 | both halves | 1e-04 |  |
| [[SAMD4A-AS1]] | +0.43 | +0.26 / +0.34 | both halves | 4e-04 |  |
| [[SLC7A11-AS1]] | +0.43 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[FKBP14-AS1]] | +0.42 | +0.30 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC45A4]] | -0.43 | -0.38 / -0.32 | both halves | 1e-04 |  |
| [[UBR1]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[DPM2]] | -0.40 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[SLC20A1]] | -0.39 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[DELE1]] | -0.39 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[ADIPOR2]] | -0.39 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[VMP1]] | -0.38 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[SCRN2]] | -0.38 | -0.22 / -0.34 | both halves | 6e-04 |  |
| [[TMEM135]] | -0.36 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[NUP98]] | -0.36 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[SLC25A33]] | -0.36 | -0.20 / -0.35 | ⚠ not reproduced | 8e-04 |  |
| [[ARFIP1]] | -0.36 | -0.15 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[SHC1]] | -0.35 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[PTGES2]] | -0.35 | -0.25 / -0.28 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCBE1]] | B | CCBE1 activity raises PGM5P2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without CCBE1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[HDAC6]] | B | HDAC6 activity raises PGM5P2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MGLL]] | B | MGLL activity raises PGM5P2's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without MGLL | 0.067 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[GPR176]] | B | GPR176 activity raises PGM5P2's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without GPR176 | 0.079 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[PGM5P2-1]] | C | PGM5P2-1 activity raises PGM5P2's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without PGM5P2-1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | B | PGM5P2 activity raises GPR176's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 5.24× lower at baseline in the lines without PGM5P2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[NMT2]] | B | PGM5P2 activity raises NMT2's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without PGM5P2 | 0.071 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[VIM-AS1]] | B | PGM5P2 activity raises VIM-AS1's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without PGM5P2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[RBMS3]] | B | PGM5P2 activity raises RBMS3's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 3.42× lower at baseline in the lines without PGM5P2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[NOTCH2NLA]] | B | PGM5P2 activity raises NOTCH2NLA's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without PGM5P2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[PGM5P2-1]] | C | PGM5P2 activity raises PGM5P2-1's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 3.04× lower at baseline in the lines without PGM5P2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.427). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 16.7); signed map (42.0, 24.7). **Vector** length 42.7, 6.36% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.6 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.7 | -0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglucomutase 5 pseudogene 2 |
| Locus type | pseudogene |
| Location | 9p11.2 — chr9:41,039,611-41,074,448 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | AK096159 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18965) · Entrez [595135](https://www.ncbi.nlm.nih.gov/gene/595135) · Ensembl [ENSG00000277778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277778)

## Data

Gene col 15899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15899); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15899]; `tensor/DDL_lfc|DDL_z.npy` [15899]; `embed/gene_vectors.npy` [15899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15899 or target_col == 15899). Every well: [[PGM5P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGM5P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
