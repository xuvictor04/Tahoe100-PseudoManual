---
symbol: "P4HTM"
type: "gene"
col: 10931
ensembl_id: "ENSG00000178467"
name: "prolyl 4-hydroxylase, transmembrane"
location: "3p21.31"
module: 27
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# P4HTM

*prolyl 4-hydroxylase, transmembrane* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.94× (z +8.4, q 2e-14, up in 11 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.50× (z +5.4, q 1e-05, up in 19 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.630× (z -6.1, q 5e-07, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A]] (+0.57, fdr 3e-05), [[FCGRT]] (+0.56, fdr 3e-05), [[ERBB2]] (+0.55, fdr 6e-05); moves opposite to [[MACF1]] (-0.54, fdr 1e-05), [[GNPNAT1]] (-0.51, fdr 4e-05), [[FLNB]] (-0.50, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MGST2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRRFIP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.4 | 2e-14 | 11/16 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.8 | 3e-12 | 16/30 (NCI-H2030, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +5.4 | 1e-05 | 19/42 (RKO, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.0 | 1e-04 | 18/38 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.9 | 1e-04 | 17/34 (LS 180, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.3 | 0.002 | 11/24 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.008 | 11/43 (hTERT-HPNE, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.56× | +3.1 | 0.15 | 3/17 (SNU-423, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -6.1 | 5e-07 | 20/38 (COLO 205, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.648×** | -5.7 | 3e-06 | 20/42 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.682×** | -5.1 | 8e-05 | 19/43 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.689×** | -4.9 | 1e-04 | 18/42 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.699×** | -4.7 | 2e-04 | 15/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -4.7 | 2e-04 | 16/40 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.713×** | -4.5 | 6e-04 | 17/41 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.007 | 18/41 (SW1417, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -3.7 | 0.011 | 12/43 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.032 | 14/42 (HS-578T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.075 | 15/41 (C-33 A, J82, …) | top dose only |  |
| [[Trimetrexate (drug)]] 5 µM |  | 0.848× | -3.1 | 0.097 | 5/41 (SW48, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0478× (z -12.3) |
| [[J82 (line)]] | alt | 7.96 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.140× (z -10.0) |
| [[BT-474 (line)]] | alt | 9.44 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0977× (z -9.5) |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0719× (z -11.2) |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 2.80 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0435× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 7.11 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +8.7) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[SNU-423 (line)]] | alt | 6.34 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.108× (z -9.0) |
| [[A-172 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A]] | +0.57 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[FCGRT]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ERBB2]] | +0.55 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[RPRD2]] | +0.55 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[GOLGA2P5]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[HOXA3]] | +0.55 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[HNMT]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[HOXB3]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HOXB6]] | +0.53 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[HFE]] | +0.53 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[GOLGA2P5-1]] | +0.53 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[MAIP1]] | +0.52 | +0.40 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACF1]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GNPNAT1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[FLNB]] | -0.50 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PALM2AKAP2]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ERRFI1]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MSN]] | -0.49 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LRRFIP1]] | -0.49 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[FMNL2]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[RSU1]] | -0.49 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[PPP2R2C]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN10]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[AKAP13]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGST2]] | B | MGST2 activity raises P4HTM's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without MGST2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[CTSF]] | B | CTSF activity lowers P4HTM's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.17× higher at baseline in the lines without CTSF | 0.048 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[DPP7]] | C | DPP7 activity raises P4HTM's level | lines that do not express DPP7 (3) vs lines expressing it (47) | 3.24× lower at baseline in the lines without DPP7 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRFIP1]] | C | P4HTM activity raises LRRFIP1's level | lines that do not express P4HTM (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without P4HTM | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, RNASEL; its own permutation p |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.339). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.1, 29.4); signed map (38.7, -14.6). **Vector** length 59.0, 9.30% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | +0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | prolyl 4-hydroxylase, transmembrane |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,989,889-49,007,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P4H-TM, PHD4, PH4, HIFPH4, FLJ20262, EGLN4, PH-4 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXG6](https://www.uniprot.org/uniprotkb/Q9NXG6) (Transmembrane prolyl 4-hydroxylase):

> Catalyzes the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. Hydroxylates HIF1A at 'Pro-402' and 'Pro-564'. May function as a cellular oxygen sensor and, under normoxic conditions, may target HIF through the hydroxylation for proteasomal degradation via the von Hippel-Lindau ubiquitination complex.

**Summary**, from NCBI Gene [54681](https://www.ncbi.nlm.nih.gov/gene/54681):

> The product of this gene belongs to the family of prolyl 4-hydroxylases. This protein is a prolyl hydroxylase that may be involved in the degradation of hypoxia-inducible transcription factors under normoxia. It plays a role in adaptation to hypoxia and may be related to cellular oxygen sensing. Alternatively spliced variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28858) · Entrez [54681](https://www.ncbi.nlm.nih.gov/gene/54681) · UniProt [Q9NXG6](https://www.uniprot.org/uniprotkb/Q9NXG6) · Ensembl [ENSG00000178467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178467)

## Data

Gene col 10931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10931); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10931]; `tensor/DDL_lfc|DDL_z.npy` [10931]; `embed/gene_vectors.npy` [10931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10931 or target_col == 10931). Every well: [[P4HTM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P4HTM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
