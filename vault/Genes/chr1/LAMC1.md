---
symbol: "LAMC1"
type: "gene"
col: 5768
ensembl_id: "ENSG00000135862"
name: "laminin subunit gamma 1"
location: "1q25.3"
module: 78
arm: "+"
pooled_cpm: 280.25
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# LAMC1

*laminin subunit gamma 1* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.59× (z +8.9, q 4e-16, up in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.00× (z +7.2, q 1e-10, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.412× (z -17.7, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD59]] (+0.68, fdr 7e-06), [[FLNA]] (+0.67, fdr 1e-05), [[STMP1]] (+0.66, fdr 2e-05); moves opposite to [[RPAIN]] (-0.60, fdr 1e-05), [[SNHG7]] (-0.59, fdr 1e-05), [[TARS2]] (-0.58, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[VIM-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Digitoxin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.9 | 4e-16 | 29/42 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.5 | 4e-15 | 33/46 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +7.2 | 1e-10 | 34/46 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 7e-09 | 37/45 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +6.0 | 2e-07 | 28/43 (C-33 A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +5.5 | 3e-06 | 31/45 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.9 | 7e-05 | 29/45 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.006 | 22/45 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5768.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.412×** | -17.7 | 0e+00 | 39/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.526×** | -12.8 | 4e-35 | 40/45 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -11.0 | 4e-26 | 37/45 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -9.2 | 3e-18 | 28/45 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -6.0 | 2e-07 | 28/44 (SW 900, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.779×** | -5.0 | 6e-05 | 24/45 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.804×** | -4.4 | 0.001 | 28/45 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.820×** | -4.0 | 0.005 | 23/45 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.842× | -3.4 | 0.037 | 20/45 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.888× | -3.4 | 0.044 | 6/45 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.850× | -3.3 | 0.056 | 15/45 (SW 1271, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.056 | 19/45 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.853× | -3.2 | 0.065 | 20/45 (J82, NCI-H23, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.851× | -3.1 | 0.075 | 19/46 (NCI-H2030, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 499 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -12.4) |
| [[A498 (line)]] | wt | 347 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.4) | — |
| [[A549 (line)]] | wt | 344 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +10.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -15.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.374× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 3 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +14.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.267× (z -18.6) |
| [[C32 (line)]] | wt | 236 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 250 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -25.6) |
| [[NCI-H1792 (line)]] | alt | 329 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 172 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.395× (z -13.4) |
| [[SW480 (line)]] | alt | 130 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.286× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 253 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.5) |
| [[HOP62 (line)]] | alt | 519 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.7) |
| [[LoVo (line)]] | wt | 171 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 5.49× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.219× (z -20.4) |
| [[LS 180 (line)]] | wt | 88.1 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.297× (z -13.4) |
| [[RKO (line)]] | wt | 190 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -14.2) |
| [[Hs 766T (line)]] | wt | 528 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -16.8) |
| [[HT-29 (line)]] | alt | 97.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 251 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 244 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -14.3) |
| [[SNU-423 (line)]] | alt | 322 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -12.2) |
| [[SW1417 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -13.8) |
| [[H4 (line)]] | wt | 392 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.1) |
| [[HS-578T (line)]] | alt | 674 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 717 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 304 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 609 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -18.0) |
| [[SW48 (line)]] | wt | 181 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.412× (z -8.7) |
| [[A-172 (line)]] | wt | 602 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -10.4) |
| [[A-427 (line)]] | wt | 189 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.84× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 210 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.505× (z -9.2) |
| [[PANC-1 (line)]] | alt | 203 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 292 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -9.0) |
| [[SW 900 (line)]] | alt | 350 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -10.4) ⚠ toxic |
| [[BT-474 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 334 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 534 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 494 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD59]] | +0.68 | +0.70 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FLNA]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[STMP1]] | +0.66 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[CAPN2]] | +0.65 | +0.60 / +0.74 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[ITGB1]] | +0.63 | +0.71 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 982 |
| [[MSN]] | +0.63 | +0.60 / +0.70 | both halves | 7e-06 | pathway: L1CAM interactions |
| [[CD44]] | +0.62 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 922 |
| [[FSTL1]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 557 |
| [[ANXA5]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MACF1]] | +0.60 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[KPNA4]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CDC42]] | +0.60 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAIN]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TARS2]] | -0.58 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[GOLPH3L]] | -0.58 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | -0.57 | -0.37 / -0.58 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TTC38]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | -0.54 | -0.42 / -0.52 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AFMID]] | -0.54 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[C15orf61]] ⚠ | -0.54 | -0.26 / -0.62 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[LSM2]] | -0.54 | -0.11 / -0.68 | ⚠ one half (not replicated) | 0.002 |  |
| [[RPP21]] | -0.53 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[TMEM216]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[TADA1]] | -0.53 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[SAT2]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CC2D1A]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VIM-AS1]] | B | VIM-AS1 activity raises LAMC1's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 3.26× lower at baseline in the lines without VIM-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |
| [[IGFBP7]] | B | IGFBP7 activity raises LAMC1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without IGFBP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |
| [[COL6A1]] | B | COL6A1 activity raises LAMC1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without COL6A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[HDAC6]] | B | HDAC6 activity raises LAMC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC16A2]] | B | SLC16A2 activity raises LAMC1's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without SLC16A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Digitoxin (drug)]] 5 µM | C | LAMC1 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express LAMC1 (3) vs lines expressing it (45) | the lines without LAMC1: 0.52× the cells of the other lines | 0.047 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SLC36A4, CLTCL1, PALS2 |
| cells under [[Pimozide (drug)]] 0.05 µM | C | LAMC1 activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express LAMC1 (3) vs lines expressing it (45) | the lines without LAMC1: 1.26× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SLC36A4, CLTCL1, PALS2 |
| cells under [[AT7519 (drug)]] 5 µM | C | LAMC1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express LAMC1 (3) vs lines expressing it (45) | the lines without LAMC1: 0.54× the cells of the other lines | 0.086 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SLC36A4, CLTCL1, PALS2 |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.6, 7.3); signed map (-6.2, 36.5). **Vector** length 129, 41.2% of its response variance represented; |z| ≥ 3 in 1,271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.8 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -6.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -9.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.6 | -2.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,023,420-183,145,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LAMB2 |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 25 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P11047](https://www.uniprot.org/uniprotkb/P11047) (Laminin subunit gamma-1):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. As a subunit of laminin-1 (also known as laminin-111 or EHS laminin), it is involved in the stimulation of agrin-induced receptor clustering through a MuSK-independent pathway.

**Summary**, from NCBI Gene [3915](https://www.ncbi.nlm.nih.gov/gene/3915):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively), have a cruciform structure consisting of 3 short arms, each formed by a different chain, and a …

**Accessions** — [HGNC:6492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6492) · Entrez [3915](https://www.ncbi.nlm.nih.gov/gene/3915) · UniProt [P11047](https://www.uniprot.org/uniprotkb/P11047) · Ensembl [ENSG00000135862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135862)

## Data

Gene col 5768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5768); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5768]; `tensor/DDL_lfc|DDL_z.npy` [5768]; `embed/gene_vectors.npy` [5768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5768 or target_col == 5768). Every well: [[LAMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
