---
symbol: "TYRO3"
type: "gene"
col: 1700
ensembl_id: "ENSG00000092445"
name: "TYRO3 protein tyrosine kinase"
location: "15q15.1"
module: 18
arm: "+"
pooled_cpm: 6.41
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TYRO3

*TYRO3 protein tyrosine kinase* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.39× (z +12.8, q 7e-35, up in 7 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.17× (z +11.9, q 4e-30, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.508× (z -5.4, q 3e-05, down in 14 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE2]] (+0.68, fdr 7e-06), [[ADCY3]] (+0.66, fdr 7e-06), [[MSI1]] (+0.62, fdr 1e-05); moves opposite to [[C4orf33]] (-0.48, fdr 3e-05), [[ATP7A]] (-0.47, fdr 5e-05), [[RNF5]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +12.8 | 7e-35 | 7/13 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +11.9 | 4e-30 | 35/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.5 | 3e-28 | 27/41 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +10.9 | 2e-25 | 19/31 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.96×** | +10.3 | 7e-23 | 27/45 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +8.8 | 9e-17 | 25/44 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +7.5 | 4e-12 | 20/43 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +7.4 | 8e-12 | 11/22 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.1 | 9e-11 | 16/40 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.54×** | +6.4 | 1e-08 | 15/33 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +6.1 | 6e-08 | 15/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +6.0 | 8e-08 | 19/46 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 5e-07 | 9/45 (NCI-H460, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.4 | 2e-06 | 15/33 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.3 | 3e-06 | 11/30 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 5e-06 | 12/46 (LS 180, SW 900, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.0 | 1e-05 | 9/45 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 10/45 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 2e-04 | 12/45 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[vincristine (drug)]] 5 µM |  | **1.73×** | +4.4 | 3e-04 | 3/33 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +4.3 | 4e-04 | 10/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 5e-04 | 8/44 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -5.4 | 3e-05 | 14/44 (LOX-IMVI, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.577×** | -4.4 | 0.003 | 13/37 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.766×** | -4.0 | 0.015 | 14/44 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.078 | 9/45 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.813× | -3.1 | 0.22 | 8/46 (CHP-212, Hs 766T, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.685× | -3.0 | 0.22 | 6/38 (A-427, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.27 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0597× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 9.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.6) |
| [[J82 (line)]] | alt | 8.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 3.39 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0751× (z -8.5) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 4.38 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0829× (z -8.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 8.37 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.129× (z -8.9) |
| [[A-172 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE2]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MSI1]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PXYLP1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MICALL1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PKN3]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SLC22A15]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[C16orf74]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PPP2R2C]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FAXC]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ECPAS]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[MPP3]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf33]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[RNF5]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DBP]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[EID1]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.45 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[CA9]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises TYRO3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.14× lower at baseline in the lines without EBF4 | 0.063 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[GALNT14]] | B | GALNT14 activity lowers TYRO3's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.30× higher at baseline in the lines without GALNT14 | 0.074 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[ADCY3]] | B | ADCY3 activity raises TYRO3's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.14× lower at baseline in the lines without ADCY3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[PKN3]] | C | PKN3 activity raises TYRO3's level | lines that do not express PKN3 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without PKN3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUDT7, ITPKA, DNM1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (6.3, 34.8); signed map (-7.6, 26.4). **Vector** length 72.5, 11.9% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.5 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +4.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -4.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TYRO3 protein tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,557,675-41,583,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dtk, Brt, Tif, Sky, Etk-2, Rek; previously RSE |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; AXL receptor tyrosine kinase family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Dengue Virus Attachment and Entry; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06418](https://www.uniprot.org/uniprotkb/Q06418) (Tyrosine-protein kinase receptor TYRO3):

> Receptor tyrosine kinase that transduces signals from the extracellular matrix into the cytoplasm by binding to several ligands including PROS1, TULP1 or GAS6. Regulates many physiological processes including cell survival, migration and differentiation (By similarity). Ligand binding at the cell surface induces dimerization and autophosphorylation of TYRO3 on its intracellular domain that provides docking sites for downstream signaling molecules (By similarity). Following activation by ligand, …

**Summary**, from NCBI Gene [7301](https://www.ncbi.nlm.nih.gov/gene/7301):

> The gene is part of a 3-member transmembrane receptor kinase receptor family with a processed pseudogene distal on chromosome 15. The encoded protein is activated by the products of the growth arrest-specific gene 6 and protein S genes and is involved in controlling cell survival and proliferation, spermatogenesis, immunoregulation and phagocytosis. The encoded protein has also been identified as a cell entry factor for Ebola and Marburg viruses. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:12446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12446) · Entrez [7301](https://www.ncbi.nlm.nih.gov/gene/7301) · UniProt [Q06418](https://www.uniprot.org/uniprotkb/Q06418) · Ensembl [ENSG00000092445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092445)

## Data

Gene col 1700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1700); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1700]; `tensor/DDL_lfc|DDL_z.npy` [1700]; `embed/gene_vectors.npy` [1700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1700 or target_col == 1700). Every well: [[TYRO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYRO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
