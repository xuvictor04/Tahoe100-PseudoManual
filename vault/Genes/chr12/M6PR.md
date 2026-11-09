---
symbol: "M6PR"
type: "gene"
col: 27
ensembl_id: "ENSG00000003056"
name: "mannose-6-phosphate receptor, cation dependent"
location: "12p13.31"
module: 29
arm: "+"
pooled_cpm: 42.48
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# M6PR

*mannose-6-phosphate receptor, cation dependent* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.59× (z +19.0, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +18.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.809× (z -4.1, q 0.021, down in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.831× (z -3.6, q 0.087, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.0806×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMX1]] (+0.68, fdr 7e-06), [[MOB1A]] (+0.67, fdr 1e-05), [[CD164]] (+0.67, fdr 1e-05); moves opposite to [[DENND6B]] (-0.63, fdr 1e-05), [[RP9]] (-0.62, fdr 1e-05), [[SUGP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 27.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.59×** | +19.0 | 0e+00 | 46/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +18.5 | 0e+00 | 46/48 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +15.8 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.24×** | +15.4 | 0e+00 | 36/40 (SK-MEL-2, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.06×** | +13.3 | 5e-38 | 39/44 (NCI-H2030, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +11.6 | 2e-29 | 43/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +11.2 | 3e-27 | 42/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.73×** | +10.9 | 8e-26 | 39/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +10.3 | 6e-23 | 42/48 (CFPAC-1, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +10.1 | 5e-22 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.67×** | +9.7 | 1e-20 | 41/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +9.4 | 3e-19 | 4/48 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.3 | 7e-19 | 36/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.48×** | +7.8 | 3e-13 | 35/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +7.8 | 3e-13 | 36/47 (HS-578T, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 9e-07 | 30/48 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +5.2 | 5e-06 | 29/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +5.2 | 5e-06 | 25/47 (J82, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +5.1 | 6e-06 | 24/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +4.9 | 2e-05 | 25/46 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 4e-05 | 26/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.5 | 1e-04 | 19/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 3e-04 | 21/47 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 27.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.809×** | -4.1 | 0.021 | 24/47 (NCI-H2030, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.087 | 15/47 (SW 1271, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.18 | 13/48 (A-427, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 27. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.2 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 30.5 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 34.8 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 41.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 27.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.06× (z +10.0) | — |
| [[SW480 (line)]] | alt | 57.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.9) | — |
| [[A498 (line)]] | wt | 37.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[J82 (line)]] | alt | 51.0 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 56.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.2) | — |
| [[A549 (line)]] | wt | 45.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 37.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 20.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 69.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +14.5) | — |
| [[NCI-H23 (line)]] | alt | 96.2 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.3) | — |
| [[A-172 (line)]] | wt | 19.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[A-427 (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 69.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.4) | — |
| [[C32 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 35.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +8.7) | — |
| [[H4 (line)]] | wt | 47.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +8.9) | — |
| [[LoVo (line)]] | wt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0806× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 38.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.84× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 47.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 27), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[MOB1A]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CD164]] | +0.67 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.66 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[ERLIN2]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GBA1]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism |
| [[HCFC1]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PPT1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 480 |
| [[NXT2]] | +0.63 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[GNS]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: Lysosome Vesicle Biogenesis; STRING 535 |
| [[CERS2]] | +0.61 | +0.40 / +0.55 | both halves | 5e-05 | pathway: Sphingolipid metabolism |
| [[IGF2R]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 991 |

## Genes that move opposite

*50 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND6B]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[RP9]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SUGP1]] | -0.62 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[LIN7B]] | -0.61 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | -0.60 | -0.50 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTIF3]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZFAND2B]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.59 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SSNA1]] | -0.59 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[RPP21]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[MPHOSPH10]] | -0.57 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[R3HCC1]] | -0.57 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers M6PR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-30.1, -22.1); signed map (-18.9, -37.6). **Vector** length 104, 28.5% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.2 | +15.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.7 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +5.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.2 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mannose-6-phosphate receptor, cation dependent |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,940,361-8,949,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD-MPR, CD-M6PR |
| Gene groups (HGNC) | MRH domain containing |
| Hallmark sets | PROTEIN_SECRETION, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: Glycosphingolipid catabolism; Lysosome Vesicle Biogenesis; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P20645](https://www.uniprot.org/uniprotkb/P20645) (Cation-dependent mannose-6-phosphate receptor):

> Transport of phosphorylated lysosomal enzymes from the Golgi complex and the cell surface to lysosomes. Lysosomal enzymes bearing phosphomannosyl residues bind specifically to mannose-6-phosphate receptors in the Golgi apparatus and the resulting receptor-ligand complex is transported to an acidic prelyosomal compartment where the low pH mediates the dissociation of the complex.

**Summary**, from NCBI Gene [4074](https://www.ncbi.nlm.nih.gov/gene/4074):

> This gene encodes a member of the P-type lectin family. P-type lectins play a critical role in lysosome function through the specific transport of mannose-6-phosphate-containing acid hydrolases from the Golgi complex to lysosomes. The encoded protein functions as a homodimer and requires divalent cations for ligand binding. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. A pseudogene of this gene is located on the long arm of chromosome X. …

**Accessions** — [HGNC:6752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6752) · Entrez [4074](https://www.ncbi.nlm.nih.gov/gene/4074) · UniProt [P20645](https://www.uniprot.org/uniprotkb/P20645) · Ensembl [ENSG00000003056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003056)

## Data

Gene col 27: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 27); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 27, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 27]; `tensor/DDL_lfc|DDL_z.npy` [27]; `embed/gene_vectors.npy` [27]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 27 or target_col == 27). Every well: [[M6PR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/M6PR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
