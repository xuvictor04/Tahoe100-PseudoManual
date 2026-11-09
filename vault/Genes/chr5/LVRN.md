---
symbol: "LVRN"
type: "gene"
col: 10313
ensembl_id: "ENSG00000172901"
name: "laeverin"
location: "5q23.1"
module: 37
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# LVRN

*laeverin* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +10.7, q 6e-24, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.478× (z -7.2, q 3e-10, down in 25 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Berbamine (drug)]] 0.05 µM: 0.648× (z -4.4, q 0.003, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00640]] (+0.79, fdr 7e-06), [[WDR49]] (+0.74, fdr 7e-06), [[SNX31]] (+0.69, fdr 1e-05); moves opposite to [[RNFT2]] (-0.58, fdr 1e-04), [[ZFAND4]] (-0.50, fdr 1e-04), [[CHCHD6]] (-0.50, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CASC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +10.7 | 6e-24 | 22/42 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.73×** | +10.2 | 6e-22 | 38/46 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +8.4 | 1e-14 | 28/40 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.9 | 3e-13 | 25/40 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +7.2 | 6e-11 | 22/41 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +7.2 | 6e-11 | 21/40 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +6.7 | 2e-09 | 28/44 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.52×** | +6.7 | 2e-09 | 36/44 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +6.5 | 4e-09 | 25/45 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +6.2 | 3e-08 | 24/45 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +5.9 | 1e-07 | 26/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.91×** | +5.7 | 7e-07 | 14/22 (NCI-H1573, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 4e-06 | 23/40 (AsPC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.35×** | +4.3 | 8e-04 | 17/46 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.010 | 10/45 (HEC-1-A, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.016 | 11/44 (SK-MEL-2, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.019 | 14/43 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.021 | 14/44 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.478×** | -7.2 | 3e-10 | 25/37 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.648×** | -4.4 | 0.003 | 17/45 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.653×** | -4.3 | 0.003 | 18/32 (NCI-H1573, hTERT-HPNE, …) | two highest doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.658×** | -4.2 | 0.003 | 18/45 (A498, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -4.2 | 0.003 | 20/42 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.671×** | -4.0 | 0.005 | 14/45 (SW 1088, AN3 CA, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.005 | 16/46 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.691×** | -3.7 | 0.013 | 11/45 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.702×** | -3.6 | 0.021 | 11/45 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.704×** | -3.6 | 0.021 | 9/45 (PANC-1, HCT15, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.022 | 17/46 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.735×** | -3.1 | 0.081 | 16/45 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.0 | 0.081 | 17/44 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.728×** | -3.0 | 0.081 | 13/45 (HS-578T, HOP62, …) | inconsistent across doses | position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.741×** | -3.0 | 0.081 | 11/46 (NCI-H1573, CHP-212, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.742×** | -3.0 | 0.081 | 9/45 (SW 1271, AN3 CA, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.742×** | -3.0 | 0.081 | 12/45 (SW48, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 47.5 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +21.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0359× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 8.56 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +14.1) | — |
| [[SW480 (line)]] | alt | 8.03 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0926× (z -16.7) ⚠ toxic |
| [[H4 (line)]] | wt | 41.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0615× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 5.05 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.5) | — |
| [[A-172 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.3) | — |
| [[A549 (line)]] | wt | 5.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 8.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0864× (z -9.3) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 5.24 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0697× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 5.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 8.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +11.3) | — |
| [[SW48 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +10.4) | — |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00640]] | +0.79 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[WDR49]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SNX31]] | +0.69 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CMYA5]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[LEPR]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TPTE2]] | +0.67 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[ADAM20P1]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TNFSF13B]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.65 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MGC4859]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNFT2]] | -0.58 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[ZFAND4]] | -0.50 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CHCHD6]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ELP6]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[PLAA]] | -0.49 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[MINDY4]] | -0.49 | -0.49 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises LVRN's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without CASC20 | 0.009 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, -17.9); signed map (10.8, 4.9). **Vector** length 94.6, 20.8% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.5 | +10.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | laeverin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:115,962,454-116,027,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APQ, FLJ90650, AQPEP, TAQPEP |
| Gene groups (HGNC) | Aminopeptidases; M1 metallopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Q4G3](https://www.uniprot.org/uniprotkb/Q6Q4G3) (Aminopeptidase Q):

> Metalloprotease which may be important for placentation by regulating biological activity of key peptides at the embryo-maternal interface. On synthetic substrates it shows a marked preference for Leu-4-methylcoumaryl-7-amide (Leu-MCA) over Met-MCA, Arg-LCA and Lys-LCA. Cleaves the N-terminal amino acid of several peptides such as angiotensin-3, kisspeptin-10 and endokinin C.

**Summary**, from NCBI Gene [206338](https://www.ncbi.nlm.nih.gov/gene/206338):

> Predicted to enable metalloaminopeptidase activity. Predicted to be involved in peptide catabolic process and proteolysis. Predicted to be located in membrane. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26904) · Entrez [206338](https://www.ncbi.nlm.nih.gov/gene/206338) · UniProt [Q6Q4G3](https://www.uniprot.org/uniprotkb/Q6Q4G3) · Ensembl [ENSG00000172901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172901)

## Data

Gene col 10313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10313); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10313]; `tensor/DDL_lfc|DDL_z.npy` [10313]; `embed/gene_vectors.npy` [10313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10313 or target_col == 10313). Every well: [[LVRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LVRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
