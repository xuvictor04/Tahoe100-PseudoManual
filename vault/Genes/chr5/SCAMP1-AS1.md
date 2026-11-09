---
symbol: "SCAMP1-AS1"
type: "gene"
col: 14433
ensembl_id: "ENSG00000245556"
name: "SCAMP1 antisense RNA 1"
location: "5q14.1"
module: 32
arm: "+"
pooled_cpm: 4.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SCAMP1-AS1

*SCAMP1 antisense RNA 1* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +9.9, q 3e-20, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.416× (z -8.5, q 1e-14, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.84, fdr 7e-06), [[TRIM21]] (+0.76, fdr 7e-06), [[IFIH1]] (+0.75, fdr 7e-06); moves opposite to [[LPCAT4]] (-0.62, fdr 8e-05), [[TCF3]] (-0.62, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TRANK1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +9.9 | 3e-20 | 27/39 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.5 | 1e-11 | 3/7 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.2 | 9e-08 | 23/45 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.7 | 2e-06 | 10/24 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.9 | 1e-04 | 13/39 (A-172, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.6 | 3e-04 | 19/45 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.8 | 0.014 | 10/29 (LS 180, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.017 | 11/37 (A-427, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.029 | 5/46 (SHP-77, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.029 | 16/43 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.029 | 9/41 (A549, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.037 | 6/47 (NCI-H2347, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.037 | 8/41 (NCI-H23, A549, …) | rises with dose | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.87×** | +3.2 | 0.056 | 2/30 (COLO 205, KATO III) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.056 | 8/28 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.061 | 7/37 (A-172, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.416×** | -8.5 | 1e-14 | 28/46 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -8.0 | 4e-13 | 29/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -7.3 | 5e-11 | 30/45 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -4.4 | 0.001 | 17/43 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.632×** | -4.4 | 0.001 | 19/47 (H4, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.637×** | -4.3 | 0.001 | 12/38 (SNU-423, NCI-H460, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -4.3 | 0.002 | 16/47 (RPMI-7951, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -4.0 | 0.005 | 16/36 (SNU-423, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.006 | 12/41 (A549, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.015 | 16/45 (RKO, MIA PaCa-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -3.6 | 0.017 | 15/39 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.029 | 15/45 (A549, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.029 | 12/44 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -3.3 | 0.044 | 10/21 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.722×** | -3.1 | 0.071 | 12/43 (SW48, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.81 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0589× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 6.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 4.74 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0607× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0627× (z -10.5) |
| [[SW480 (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.84 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[IFIT2]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PARP14]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[IFIT5]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[PHF11]] | +0.74 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PLEKHA4]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[NMI]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[DTX3L]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TAPBPL]] | +0.72 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[RBM43]] | +0.71 | +0.57 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.62 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[TCF3]] | -0.62 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRANK1]] | C | SCAMP1-AS1's natural level strengthens TRANK1's drug response | SCAMP1-AS1's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.14; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 54.0); signed map (62.3, 32.4). **Vector** length 75.4, 14.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.57 to 56); *interferon gamma response* (hallmark, mean cos +0.58 to 60); *interferon* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | -8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -4.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SCAMP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.1 — chr5:78,342,333-78,360,507 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50544) · Entrez [728769](https://www.ncbi.nlm.nih.gov/gene/728769) · Ensembl [ENSG00000245556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245556)

## Data

Gene col 14433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14433); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14433]; `tensor/DDL_lfc|DDL_z.npy` [14433]; `embed/gene_vectors.npy` [14433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14433 or target_col == 14433). Every well: [[SCAMP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
