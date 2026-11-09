---
symbol: "RASGEF1A"
type: "gene"
col: 12735
ensembl_id: "ENSG00000198915"
name: "RasGEF domain family member 1A"
location: "10q11.21"
module: 128
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 25
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 23
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# RASGEF1A

*RasGEF domain family member 1A* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.05× (z +11.8, q 3e-29, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +7.5, q 1e-11, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.569× (z -5.0, q 4e-04, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KANK3]] (+0.62, fdr 1e-05), [[JPH3]] (+0.60, fdr 1e-05), [[KNDC1]] (+0.58, fdr 1e-05); moves opposite to [[CFAP44]] (-0.43, fdr 1e-04), [[DECR1]] (-0.42, fdr 6e-05), [[SEMA5A]] (-0.41, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SEMA5A]] → it (grade B ⚠); 23 go from it, the strongest it → [[SLC46A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +11.8 | 3e-29 | 1/6 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.4 | 1e-18 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.2 | 5e-14 | 1/6 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.5 | 1e-11 | 2/15 (A549, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +6.0 | 2e-07 | 6/20 (CFPAC-1, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +5.8 | 5e-07 | 3/9 (HEC-1-A, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.3 | 9e-06 | 6/20 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.6 | 3e-04 | 1/11 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 1e-03 | 5/15 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +3.9 | 0.004 | 2/10 (NCI-H23, HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.007 | 3/17 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.7 | 0.010 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.011 | 3/21 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.4 | 0.026 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.3 | 0.040 | 1/14 (A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.040 | 5/20 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.02×** | +3.2 | 0.044 | 0/11 | rises with dose | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.044 | 0/15 | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.048 | 3/15 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.049 | 4/14 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.049 | 1/15 (NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.0 | 0.057 | 2/13 (SW480, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.063 | 3/15 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.063 | 3/20 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -5.0 | 4e-04 | 11/21 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **0.585×** | -4.7 | 6e-04 | 4/21 (HCT15, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | **0.608×** | -4.4 | 0.002 | 1/21 (NCI-H1792) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.612×** | -4.0 | 0.008 | 2/19 (NCI-H1792, SW 900) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.702× | -3.1 | 0.19 | 11/19 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.1) |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 7.52 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0730× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.213× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 2.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0807× (z -11.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 1.92 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0771× (z -8.5) |
| [[A-172 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.289 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANK3]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[JPH3]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[KNDC1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ADGRB1]] | +0.57 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[LRRC36]] | +0.54 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[RFPL1S]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LPAR3]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[HES2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[EPHA10]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MYO15B]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[JAG2]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[KIF1A]] | +0.52 | +0.49 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP44]] | -0.43 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[DECR1]] | -0.42 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[SEMA5A]] | -0.41 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA5A]] | B | SEMA5A activity lowers RASGEF1A's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.70× higher at baseline in the lines without SEMA5A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[ABCA17P]] | B | ABCA17P activity raises RASGEF1A's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without ABCA17P | 0.078 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[RFPL1S]] | B | RFPL1S activity raises RASGEF1A's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without RFPL1S | 0.079 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises RASGEF1A's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without LINC02026 | 0.091 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[NR5A2]] | C | NR5A2 activity raises RASGEF1A's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without NR5A2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[ANKRD20A11P]] | C | ANKRD20A11P activity raises RASGEF1A's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without ANKRD20A11P | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises RASGEF1A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without CHD5 | 0.066 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[EPHA10]] | C | EPHA10 activity raises RASGEF1A's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without EPHA10 | 0.071 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2; co-absent with the target |
| [[PAX2]] | C | PAX2 activity raises RASGEF1A's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without PAX2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 17, C 6. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC46A1]] | B | RASGEF1A activity raises SLC46A1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without RASGEF1A | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[SLC29A2]] | B | RASGEF1A activity raises SLC29A2's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without RASGEF1A | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[BMP8B]] | B | RASGEF1A activity raises BMP8B's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without RASGEF1A | 0.023 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[NUDT7]] | B | RASGEF1A activity raises NUDT7's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without RASGEF1A | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[KCNK15-AS1]] | B | RASGEF1A activity raises KCNK15-AS1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without RASGEF1A | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[CCDC120]] | B | RASGEF1A activity raises CCDC120's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without RASGEF1A | 0.029 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[DOC2A]] | B | RASGEF1A activity raises DOC2A's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.96× lower at baseline in the lines without RASGEF1A | 0.029 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[LINC02026]] | B | RASGEF1A activity raises LINC02026's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without RASGEF1A | 0.030 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[FBXO15]] | B | RASGEF1A activity raises FBXO15's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without RASGEF1A | 0.033 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[KCNK15-AS1]] | B | RASGEF1A activity strengthens KCNK15-AS1's drug response | lines that do not express RASGEF1A (21) vs lines expressing it (20) | the lines without RASGEF1A respond 0.70× as strongly (z diff +1.17); strongest at Homoharringtonine 5 µM: 0.37x vs 0.15x (z diff +4.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB; target measured in part of the lines; artifact flags |
| [[DOCK3]] | B | RASGEF1A activity raises DOCK3's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without RASGEF1A | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[CHST10]] | B | RASGEF1A activity raises CHST10's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without RASGEF1A | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, 37.9); signed map (24.3, 25.1). **Vector** length 43.0, 9.50% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.5 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RasGEF domain family member 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:43,194,535-43,267,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CG4853, FLJ37817 |
| Reactome | 3 pathways, smallest: RAF/MAP kinase cascade; MAPK1/MAPK3 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9B8](https://www.uniprot.org/uniprotkb/Q8N9B8) (Ras-GEF domain-containing family member 1A):

> Guanine nucleotide exchange factor (GEF) with specificity for RAP2A, KRAS, HRAS, and NRAS (in vitro). Plays a role in cell migration.

**Summary**, from NCBI Gene [221002](https://www.ncbi.nlm.nih.gov/gene/221002):

> Enables guanyl-nucleotide exchange factor activity. Involved in cell migration and positive regulation of Ras protein signal transduction. Predicted to be located in cytosol. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24246) · Entrez [221002](https://www.ncbi.nlm.nih.gov/gene/221002) · UniProt [Q8N9B8](https://www.uniprot.org/uniprotkb/Q8N9B8) · Ensembl [ENSG00000198915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198915)

## Data

Gene col 12735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12735); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12735]; `tensor/DDL_lfc|DDL_z.npy` [12735]; `embed/gene_vectors.npy` [12735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12735 or target_col == 12735). Every well: [[RASGEF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGEF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
