---
symbol: "DOCK9"
type: "gene"
col: 1533
ensembl_id: "ENSG00000088387"
name: "dedicator of cytokinesis 9"
location: "13q32.3"
module: 193
arm: "+"
pooled_cpm: 113.5
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# DOCK9

*dedicator of cytokinesis 9* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +8.0, q 7e-13, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.606× (z -14.0, q 1e-41, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.805× (z -6.1, q 9e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN14]] (+0.64, fdr 1e-05), [[FMNL2]] (+0.63, fdr 1e-05), [[ACOT7]] (+0.63, fdr 7e-06); moves opposite to [[COPS5]] (-0.60, fdr 1e-05), [[NDUFA5]] (-0.60, fdr 1e-05), [[COG4]] (-0.59, fdr 1e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.0 | 7e-13 | 28/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.5 | 2e-08 | 31/47 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 3e-04 | 22/47 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.002 | 23/48 (HEC-1-A, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.003 | 25/47 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.009 | 23/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.031 | 12/47 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.045 | 18/46 (AsPC-1, RPMI-7951, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.606×** | -14.0 | 1e-41 | 35/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -10.9 | 4e-25 | 30/41 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.567×** | -10.3 | 2e-22 | 38/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.586×** | -10.2 | 4e-22 | 34/47 (MIA PaCa-2, RKO, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.598×** | -9.4 | 7e-19 | 33/42 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.720×** | -6.5 | 7e-09 | 30/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.728×** | -6.3 | 3e-08 | 36/47 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -6.1 | 9e-08 | 26/47 (NCI-H2347, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -6.0 | 1e-07 | 28/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.741×** | -5.4 | 3e-06 | 26/47 (SW48, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.773×** | -5.1 | 2e-05 | 24/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.772×** | -4.9 | 4e-05 | 25/46 (MIA PaCa-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.652×** | -4.4 | 4e-04 | 25/46 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.825×** | -3.8 | 0.006 | 23/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.010 | 18/48 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.860× | -3.6 | 0.013 | 17/47 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.6 | 2 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +13.7) | [[Harringtonine (drug)]] 0.5 µM 0.380× (z -11.1) ⚠ cell-cycle shift, explains ~20% of this change |
| [[LoVo (line)]] | wt | 110 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -14.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.5 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.244× (z -15.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 199 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 176 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.92× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 77.3 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 74.7 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -30.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C32 (line)]] | wt | 98.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +14.6) | [[Harringtonine (drug)]] 5 µM 0.326× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -13.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Hs 766T (line)]] | wt | 284 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -13.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 68.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW48 (line)]] | wt | 109 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 67.8 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.638× (z -13.0) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 95.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -18.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 76.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 81.0 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 2.95× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 2.91× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 59.0 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +10.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.8) | — |
| [[KATO III (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 76.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.9) | [[Docetaxel (drug)]] 0.05 µM 0.348× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0699× (z -10.4) |
| [[COLO 205 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.483× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 1088 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.5 µM 0.0680× (z -9.2) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0781× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.474× (z -9.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN14]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FMNL2]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 | same gene group; pathway: CDC42 GTPase cycle |
| [[ACOT7]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[EVI5]] | +0.63 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[CDYL]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RASA2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 | same gene group |
| [[CDYL2]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KANK1]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PAQR4]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[POC1B]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS5]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[COG4]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[IFT81]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[UFSP2]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H7A]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TMEM254]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ACIN1]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MTERF4]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers DOCK9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.2, 5.6); signed map (-11.9, 44.5). **Vector** length 119, 34.1% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +4.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.8 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.7 | -14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.5 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:98,793,429-99,086,625 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1058, ZIZ1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Armadillo like helical domain containing; DOCK family Rho GEFs |
| Hallmark sets | COMPLEMENT |
| Reactome | 7 pathways, smallest: Factors involved in megakaryocyte development and platelet production; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ29](https://www.uniprot.org/uniprotkb/Q9BZ29) (Dedicator of cytokinesis protein 9):

> Guanine nucleotide-exchange factor (GEF) that activates CDC42 by exchanging bound GDP for free GTP. Overexpression induces filopodia formation.

**Summary**, from NCBI Gene [23348](https://www.ncbi.nlm.nih.gov/gene/23348):

> Enables cadherin binding activity. Predicted to be involved in positive regulation of GTPase activity and regulation of Rho protein signal transduction. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14132) · Entrez [23348](https://www.ncbi.nlm.nih.gov/gene/23348) · UniProt [Q9BZ29](https://www.uniprot.org/uniprotkb/Q9BZ29) · Ensembl [ENSG00000088387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088387)

## Data

Gene col 1533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1533); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1533]; `tensor/DDL_lfc|DDL_z.npy` [1533]; `embed/gene_vectors.npy` [1533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1533 or target_col == 1533). Every well: [[DOCK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
