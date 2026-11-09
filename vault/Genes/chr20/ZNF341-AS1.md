---
symbol: "ZNF341-AS1"
type: "gene"
col: 13767
ensembl_id: "ENSG00000230753"
name: "ZNF341 antisense RNA 1"
location: "20q11.22"
module: 80
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 40
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ZNF341-AS1

*ZNF341 antisense RNA 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 15.4× (z +32.2, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.372× (z -8.3, q 8e-14, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAKMAR2]] (+0.80, fdr 7e-06), [[LPXN]] (+0.80, fdr 1e-05), [[NEK8]] (+0.79, fdr 1e-05); moves opposite to [[ELP1]] (-0.69, fdr 1e-05), [[SLC9A6]] (-0.68, fdr 7e-05), [[ACTR5]] (-0.68, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 40 go from it, the strongest it → [[MAZ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **15.4×** | +32.2 | 0e+00 | 29/29 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **8.18×** | +24.7 | 0e+00 | 27/27 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.47×** | +16.0 | 0e+00 | 21/23 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.90×** | +14.1 | 5e-43 | 27/33 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.60×** | +13.7 | 1e-40 | 25/28 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.66×** | +12.8 | 1e-35 | 24/28 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.87×** | +12.4 | 2e-33 | 27/36 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +10.5 | 4e-24 | 3/4 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +9.3 | 1e-18 | 5/7 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +8.7 | 1e-16 | 5/13 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +8.4 | 2e-15 | 20/36 (SW480, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +6.9 | 3e-10 | 24/34 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +6.4 | 6e-09 | 9/12 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +5.9 | 2e-07 | 16/34 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +5.1 | 1e-05 | 10/31 (A-172, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +4.8 | 6e-05 | 10/32 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.002 | 9/33 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.036 | 8/32 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.036 | 9/34 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.372×** | -8.3 | 8e-14 | 26/38 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -7.3 | 6e-11 | 24/35 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -6.9 | 1e-09 | 24/36 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.498×** | -5.8 | 7e-07 | 18/37 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.307×** | -5.2 | 3e-05 | 13/31 (SNU-423, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.608×** | -4.2 | 0.003 | 12/26 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fusidic acid (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.093 | 6/37 (SK-MEL-2, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 9.90 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +12.8) | [[Belinostat (drug)]] 0.5 µM 0.0516× (z -12.0) |
| [[A498 (line)]] | wt | 2.23 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +12.6) | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0644× (z -8.9) |
| [[LoVo (line)]] | wt | 2.13 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.0478× (z -9.0) |
| [[A-172 (line)]] | wt | 2.27 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 6.45 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.60× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 3.58 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +11.8) | [[Belinostat (drug)]] 5 µM 0.0421× (z -9.6) |
| [[SW480 (line)]] | alt | 1.80 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.3) | [[Panobinostat (drug)]] 0.05 µM 0.0354× (z -11.6) |
| [[HOP62 (line)]] | alt | 1.29 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 38.8× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 2.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +9.9) | — |
| [[J82 (line)]] | alt | 4.28 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.90 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 1.60 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.5× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 1.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 1.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +11.7) | — |
| [[RKO (line)]] | wt | 4.18 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.4) | [[Ixazomib citrate (drug)]] 5 µM 0.0427× (z -8.7) |
| [[SW1417 (line)]] | alt | 5.37 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.6) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0866× (z -8.7) |
| [[A549 (line)]] | wt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +11.6) | — |
| [[C32 (line)]] | wt | 1.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.6× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 4.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +12.6) | — |
| [[KATO III (line)]] | alt | 1.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.9) | — |
| [[A-427 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAKMAR2]] | +0.80 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[LPXN]] | +0.80 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[NEK8]] | +0.79 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.79 | +0.74 / +0.38 | both halves | 7e-05 | same gene group |
| [[MMADHC-DT]] | +0.78 | +0.74 / +0.40 | both halves | 4e-05 |  |
| [[LINC00863]] | +0.77 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[LETM2]] | +0.77 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.76 | +0.77 / +0.41 | both halves | 4e-05 | same gene group |
| [[BCL10-AS1]] | +0.76 | +0.74 / +0.54 | both halves | 1e-05 | same gene group |
| [[PBLD]] | +0.76 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[LINC01090]] | +0.75 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[LINC01829]] | +0.74 | +0.66 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | -0.69 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.68 | -0.70 / -0.38 | both halves | 7e-05 |  |
| [[ACTR5]] | -0.68 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CEP131]] | -0.67 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.67 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[NUDT21]] | -0.67 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MAST3]] | -0.66 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[RSAD1]] | -0.66 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[NDRG3]] | -0.66 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF341-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[WFDC3]] | B | WFDC3 activity raises ZNF341-AS1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without WFDC3 | 0.008 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[LACC1]] | B | LACC1 activity raises ZNF341-AS1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without LACC1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[LINC00944]] | B | LINC00944 activity raises ZNF341-AS1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.38× lower at baseline in the lines without LINC00944 | 0.042 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[CARD6]] | B | CARD6 activity raises ZNF341-AS1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without CARD6 | 0.047 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[HCP5]] | B | HCP5 activity raises ZNF341-AS1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.68× lower at baseline in the lines without HCP5 | 0.049 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HDAC6]] | B | HDAC6 activity raises ZNF341-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZHX2]] | C | ZHX2 activity raises ZNF341-AS1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without ZHX2 | 0.009 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1; co-absent with the target |
| [[S100A13]] | C | S100A13 activity raises ZNF341-AS1's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without S100A13 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 38, C 2. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAZ]] | B | ZNF341-AS1 activity lowers MAZ's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without ZNF341-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ICA1L]] | B | ZNF341-AS1 activity lowers ICA1L's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.21× higher at baseline in the lines without ZNF341-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[WFDC3]] | B | ZNF341-AS1 activity raises WFDC3's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without ZNF341-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[CS]] | B | ZNF341-AS1 activity lowers CS's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without ZNF341-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[MAFF]] | B | ZNF341-AS1 activity raises MAFF's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ZNF341-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ABCA10]] | B | ZNF341-AS1 activity raises ABCA10's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without ZNF341-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[S100A13]] | B | ZNF341-AS1 activity raises S100A13's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.32× lower at baseline in the lines without ZNF341-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[NAA40]] | B | ZNF341-AS1 activity lowers NAA40's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ZNF341-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[TBC1D24]] | B | ZNF341-AS1 activity lowers TBC1D24's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without ZNF341-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[NKX3-1]] | B | ZNF341-AS1 activity raises NKX3-1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without ZNF341-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[CEMIP2]] | B | ZNF341-AS1 activity raises CEMIP2's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.48× lower at baseline in the lines without ZNF341-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[SYBU]] | B | ZNF341-AS1 activity lowers SYBU's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without ZNF341-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.896). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 10.8); signed map (22.2, -5.8). **Vector** length 82.5, 17.5% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +32.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +24.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +16.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.3 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.9 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ZNF341 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.22 — chr20:33,787,373-33,811,109 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50736) · Entrez [101929746](https://www.ncbi.nlm.nih.gov/gene/101929746) · Ensembl [ENSG00000230753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230753)

## Data

Gene col 13767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13767); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13767]; `tensor/DDL_lfc|DDL_z.npy` [13767]; `embed/gene_vectors.npy` [13767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13767 or target_col == 13767). Every well: [[ZNF341-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF341-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
