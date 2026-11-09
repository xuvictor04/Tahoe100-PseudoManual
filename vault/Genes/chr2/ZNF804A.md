---
symbol: "ZNF804A"
type: "gene"
col: 9947
ensembl_id: "ENSG00000170396"
name: "zinc finger protein 804A"
location: "2q32.1"
module: 9
arm: "+"
pooled_cpm: 57.39
n_lines_expressing: 19
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ZNF804A

*zinc finger protein 804A* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +11.6, q 3e-28, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.468× (z -9.2, q 2e-17, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HECW2]] (+0.61, fdr 1e-05), [[DOCK10]] (+0.61, fdr 1e-05), [[KCNQ5]] (+0.60, fdr 1e-05); moves opposite to [[CASP9]] (-0.52, fdr 5e-05), [[DENND3]] (-0.50, fdr 1e-04), [[PLEKHH3]] (-0.50, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[CASC15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +11.6 | 3e-28 | 5/17 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +9.8 | 4e-20 | 13/16 (HS-578T, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.6 | 1e-15 | 0/16 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +6.8 | 2e-09 | 1/16 (H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.4 | 2e-08 | 0/16 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.4 | 6e-06 | 3/16 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.2 | 2e-05 | 8/15 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +5.1 | 2e-05 | 9/17 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.0 | 4e-05 | 10/16 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.3 | 9e-04 | 2/17 (BT-474, NCI-H2030) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 0/18 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.014 | 4/17 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.014 | 1/16 (BT-474) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.068 | 6/16 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.080 | 8/17 (HOP62, PANC-1, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.080 | 0/16 | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.468×** | -9.2 | 2e-17 | 17/17 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.511×** | -8.1 | 1e-13 | 16/16 (NCI-H1792, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -7.2 | 1e-10 | 16/17 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.020 | 0/17 | rises with dose |  |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | **0.658×** | -3.6 | 0.026 | 1/17 (BT-474) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.724×** | -3.6 | 0.026 | 2/16 (HepG2/C3A, BT-474) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.752×** | -3.5 | 0.039 | 3/16 (CHP-212, J82, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.039 | 8/17 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.039 | 2/18 (HepG2/C3A, BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | **0.586×** | -3.4 | 0.039 | 1/17 (HepG2/C3A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.770× | -3.1 | 0.11 | 12/17 (J82, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 152 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.13× (z +8.6) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.239× (z -10.9) |
| [[CHP-212 (line)]] | wt | 409 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0938× (z -12.2) |
| [[H4 (line)]] | wt | 155 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -11.0) |
| [[HOP62 (line)]] | alt | 103 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.93× (z +10.1) | [[Adagrasib (drug)]] 0.05 µM 0.655× (z -9.4) ⚠ position not correctable |
| [[LOX-IMVI (line)]] | wt | 252 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 276 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0751× (z -18.2) |
| [[SHP-77 (line)]] | alt | 253 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -13.4) |
| [[HS-578T (line)]] | alt | 90.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 6.29× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.209× (z -9.6) |
| [[J82 (line)]] | alt | 218 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -10.2) |
| [[A-172 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 8.61× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 399 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECW2]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DOCK10]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KCNQ5]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TOX]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NKAIN3]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ZFHX4]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 | same gene group |
| [[NR2F1-AS1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MMP16]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 | STRING 402 |
| [[CACNA2D1]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LINC00470]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[FLRT2]] | +0.58 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[DGKI]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP9]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[DENND3]] | -0.50 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[PLEKHH3]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ARL3]] | -0.49 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ORC4]] | -0.49 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[ESYT2]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[KMT5C]] | -0.48 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[IFT172]] | -0.47 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[LSM14B]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZNF804A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NETO1]] | C | NETO1 activity raises ZNF804A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 13.47× lower at baseline in the lines without NETO1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises ZNF804A's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 6.68× lower at baseline in the lines without TRPC4 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[TBX18]] | C | TBX18 activity raises ZNF804A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 4.27× lower at baseline in the lines without TBX18 | 0.043 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises ZNF804A's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 4.67× lower at baseline in the lines without SCN3A | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[LINC01684]] | C | LINC01684 activity raises ZNF804A's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without LINC01684 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC15]] | B | ZNF804A activity raises CASC15's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ZNF804A | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA |
| [[PRKACB]] | B | ZNF804A activity raises PRKACB's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without ZNF804A | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA |
| [[TCF4]] | C | ZNF804A activity raises TCF4's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 5.06× lower at baseline in the lines without ZNF804A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[HECW2]] | C | ZNF804A activity raises HECW2's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 4.22× lower at baseline in the lines without ZNF804A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[SCN3A]] | C | ZNF804A activity raises SCN3A's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without ZNF804A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[NETO1]] | C | ZNF804A activity raises NETO1's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without ZNF804A | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[MMP16]] | C | ZNF804A activity raises MMP16's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 4.18× lower at baseline in the lines without ZNF804A | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[KCNQ5]] | C | ZNF804A activity raises KCNQ5's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 5.41× lower at baseline in the lines without ZNF804A | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 25.5); signed map (40.6, 28.3). **Vector** length 69.3, 26.5% of its response variance represented; |z| ≥ 3 in 422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.5 | -8.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -9.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -7.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 804A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:184,598,529-184,939,492 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C2orf10 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZNF804 family |
| Matched by | ensembl_id |

UniProt [Q7Z570](https://www.uniprot.org/uniprotkb/Q7Z570) carries no function annotation.

**Summary**, from NCBI Gene [91752](https://www.ncbi.nlm.nih.gov/gene/91752):

> The protein encoded by this gene is a zinc finger binding protein. Polymorphisms in this gene, especially rs1344706, are thought to confer increased susceptibility to schizophrenia, bipolar disorder, and heroin addiciton. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:21711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21711) · Entrez [91752](https://www.ncbi.nlm.nih.gov/gene/91752) · UniProt [Q7Z570](https://www.uniprot.org/uniprotkb/Q7Z570) · Ensembl [ENSG00000170396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170396)

## Data

Gene col 9947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9947); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9947]; `tensor/DDL_lfc|DDL_z.npy` [9947]; `embed/gene_vectors.npy` [9947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9947 or target_col == 9947). Every well: [[ZNF804A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF804A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
