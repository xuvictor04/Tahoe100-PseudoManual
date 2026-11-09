---
symbol: "NBPF3"
type: "gene"
col: 6656
ensembl_id: "ENSG00000142794"
name: "NBPF member 3"
location: "1p36.12"
module: 30
arm: "+"
pooled_cpm: 18.37
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NBPF3

*NBPF member 3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +11.3, q 5e-27, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.496× (z -17.4, q 0e+00, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -12.6, q 6e-34, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.73, fdr 1e-05), [[PCTP]] (+0.71, fdr 7e-06), [[MFSD9]] (+0.71, fdr 7e-06); moves opposite to [[MMADHC-DT]] (-0.70, fdr 5e-05), [[TRIP12]] (-0.70, fdr 9e-06), [[CCDC90B-AS1]] (-0.70, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GATA2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +11.3 | 5e-27 | 37/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +9.7 | 6e-20 | 33/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +8.8 | 2e-16 | 29/47 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.8 | 9e-10 | 27/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.8 | 9e-10 | 24/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.27×** | +6.0 | 2e-07 | 22/47 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +4.8 | 1e-04 | 15/47 (HT-29, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.006 | 16/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.16× | +3.8 | 0.010 | 9/47 (hTERT-HPNE, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.016 | 13/47 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.22×** | +3.6 | 0.019 | 10/46 (H4, HCT15, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.023 | 12/46 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.055 | 6/47 (A-427, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.496×** | -17.4 | 0e+00 | 36/46 (HOP62, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -12.6 | 6e-34 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -12.3 | 2e-32 | 32/46 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -11.8 | 7e-30 | 35/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -9.8 | 1e-20 | 35/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -9.8 | 1e-20 | 34/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.599×** | -9.0 | 2e-17 | 26/39 (HepG2/C3A, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -8.6 | 7e-16 | 24/35 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.636×** | -7.6 | 1e-12 | 27/46 (HOP62, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -7.0 | 2e-10 | 25/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -6.8 | 5e-10 | 27/47 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -6.2 | 3e-08 | 26/47 (AN3 CA, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -6.1 | 5e-08 | 23/47 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -5.9 | 2e-07 | 24/47 (SW 1088, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.6 | 6e-07 | 25/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.590×** | -4.8 | 5e-05 | 19/45 (MIA PaCa-2, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.802×** | -3.8 | 0.004 | 14/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.005 | 13/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.043 | 9/47 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.043 | 9/47 (LoVo, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -13.3) |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -22.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -15.3) |
| [[SW480 (line)]] | alt | 30.1 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -14.2) |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.281× (z -11.4) |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -15.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.0) |
| [[C32 (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 22.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.220× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0623× (z -12.4) |
| [[A-172 (line)]] | wt | 9.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0709× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0703× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0973× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 8.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.9) |
| [[SNU-423 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.8) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.73 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[PCTP]] | +0.71 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MFSD9]] | +0.71 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DPY30]] | +0.70 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.70 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[NBPF1]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; STRING 726 |
| [[ATG4C]] | +0.69 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SCAI]] | +0.69 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.69 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.68 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[NFRKB]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.70 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[TRIP12]] | -0.70 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[CCDC90B-AS1]] | -0.70 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[TUG1]] | -0.69 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.69 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.69 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ATXN7]] | -0.69 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PATL2]] | -0.68 | -0.71 / -0.27 | both halves | 3e-04 |  |
| [[ZFX]] | -0.68 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PBLD]] | -0.68 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.63 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA2-AS1]] | B | GATA2-AS1 activity raises NBPF3's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without GATA2-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: GATA2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NBPF3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NBPF3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises NBPF3's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without WARS2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[POGLUT2]] | C | POGLUT2 activity raises NBPF3's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without POGLUT2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.7, -6.8); signed map (-35.2, -5.0). **Vector** length 84.2, 16.8% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.0 | +8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.8 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.2 | -17.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -6.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:21,440,128-21,485,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AE2 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q9H094](https://www.uniprot.org/uniprotkb/Q9H094) carries no function annotation.

**Summary**, from NCBI Gene [84224](https://www.ncbi.nlm.nih.gov/gene/84224):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. DUF1220 copy number variations in human chromosomal region …

**Accessions** — [HGNC:25076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25076) · Entrez [84224](https://www.ncbi.nlm.nih.gov/gene/84224) · UniProt [Q9H094](https://www.uniprot.org/uniprotkb/Q9H094) · Ensembl [ENSG00000142794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142794)

## Data

Gene col 6656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6656); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6656]; `tensor/DDL_lfc|DDL_z.npy` [6656]; `embed/gene_vectors.npy` [6656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6656 or target_col == 6656). Every well: [[NBPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
