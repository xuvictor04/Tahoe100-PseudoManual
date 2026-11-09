---
symbol: "STARD4"
type: "gene"
col: 8903
ensembl_id: "ENSG00000164211"
name: "StAR related lipid transfer domain containing 4"
location: "5q22.1"
module: 86
arm: "+"
pooled_cpm: 95.22
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# STARD4

*StAR related lipid transfer domain containing 4* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Berbamine (drug)]] 5 µM: 2.13× (z +12.5, q 5e-33, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.595× (z -5.9, q 3e-06, down in 31 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.616× (z -5.5, q 8e-06, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR7]] (+0.75, fdr 7e-06), [[ACSS2]] (+0.74, fdr 7e-06), [[INSIG1]] (+0.74, fdr 7e-06); moves opposite to [[ZC3H18]] (-0.52, fdr 1e-05), [[KMT2B]] (-0.50, fdr 3e-05), [[FEM1A]] (-0.49, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RADX]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RADX]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.13×** | +12.5 | 5e-33 | 44/45 (LoVo, A549, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.83×** | +10.0 | 6e-21 | 40/44 (A549, LoVo, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.8 | 1e-06 | 31/44 (LS 180, RKO, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.35×** | +5.0 | 8e-05 | 34/44 (A549, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 5e-04 | 33/45 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.014 | 30/44 (A549, HOP62, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.021 | 27/45 (A498, HOP62, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.049 | 26/44 (A549, C-33 A, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.049 | 23/44 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.052 | 19/44 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.066 | 22/45 (SHP-77, NCI-H2347, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.071 | 19/44 (LoVo, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.088 | 21/44 (LS 180, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -5.9 | 3e-06 | 31/43 (CHP-212, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.616×** | -5.5 | 8e-06 | 34/44 (LoVo, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.5 | 8e-06 | 29/45 (CHP-212, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.632×** | -5.4 | 1e-05 | 31/44 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.643×** | -4.9 | 9e-05 | 31/44 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.659×** | -4.9 | 9e-05 | 30/45 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -4.8 | 1e-04 | 27/44 (KATO III, RKO, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -4.3 | 0.001 | 29/44 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -4.3 | 0.001 | 26/44 (COLO 205, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.697×** | -4.0 | 0.004 | 26/44 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.719×** | -3.9 | 0.005 | 24/44 (SW 1088, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -3.9 | 0.005 | 24/44 (RKO, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -3.8 | 0.006 | 27/44 (RKO, LS 180, …) | top dose only | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.022 | 23/45 (KATO III, RKO, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.669×** | -3.4 | 0.027 | 26/44 (C32, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.751×** | -3.4 | 0.027 | 22/44 (H4, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 126 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.4) |
| [[RKO (line)]] | wt | 95.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.6) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -12.0) |
| [[LoVo (line)]] | wt | 104 | 2 | 2 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.79× (z +16.7) | [[Belumosudil (drug)]] 5 µM 0.312× (z -9.9) |
| [[A-427 (line)]] | wt | 676 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.02× (z +9.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[COLO 205 (line)]] | alt | 107 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.89× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -9.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 74.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 2.46× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 117 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.70× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -9.3) |
| [[LS 180 (line)]] | wt | 98.0 | 2 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 2.63× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1573 (line)]] | alt | 69.9 | 1 | 2 (1 ⚠) | [[Berbamine (drug)]] 5 µM 2.51× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.2) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.8) |
| [[A549 (line)]] | wt | 32.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.92× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 60.8 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.91× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 71.4 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.56× (z +12.3) | — |
| [[CHP-212 (line)]] | wt | 311 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -9.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.7) |
| [[H4 (line)]] | wt | 70.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Berbamine (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.74× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 56.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.53× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 41.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.51× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.326× (z -9.4) |
| [[SNU-423 (line)]] | alt | 125 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.35× (z +10.4) | — |
| [[A498 (line)]] | wt | 48.7 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.31× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 63.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.5) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -10.4) |
| [[HCT15 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[hTERT-HPNE (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.1) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.323× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 49.8 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.6) |
| [[SW 900 (line)]] | alt | 62.4 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.74× (z +9.4) | — |
| [[A-172 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR7]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 456 |
| [[ACSS2]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[INSIG1]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 576 |
| [[FDFT1]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 405 |
| [[MSMO1]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 608 |
| [[MVD]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCS1]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 660 |
| [[SCD]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCR]] | +0.69 | +0.75 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 593 |
| [[FDPS]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 503 |
| [[CYP51A1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 484 |
| [[SREBF2]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 556 |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H18]] | -0.52 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[KMT2B]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[FEM1A]] | -0.49 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[MRM3]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ITPA]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF830]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ZNF629]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TRMT5]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[NOL11]] | -0.46 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[LRRC37A4P]] | -0.46 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[C1orf109]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RADX]] | B | RADX activity raises STARD4's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without RADX | 0.093 | ⚠ within organs, on part of the lines; also absent: RNF128 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RADX]] | C | STARD4 activity raises RADX's level | lines that do not express STARD4 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without STARD4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RNF103-CHMP3; its own permutation p |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -49.1); signed map (-53.0, 32.6). **Vector** length 145, 45.6% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis* (reactome, mean cos +0.63 to 20); *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.65 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.65 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +8.7 | +10.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.3 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.7 | +2.7 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +4.9 | +3.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.0 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1 — chr5:111,496,033-111,512,590 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Pregnenolone biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DR4](https://www.uniprot.org/uniprotkb/Q96DR4) (StAR-related lipid transfer protein 4):

> Involved in the intracellular transport of cholesterol. Binds cholesterol or other sterols.

**Summary**, from NCBI Gene [134429](https://www.ncbi.nlm.nih.gov/gene/134429):

> Cholesterol homeostasis is regulated, at least in part, by sterol regulatory element (SRE)-binding proteins (e.g., SREBP1; MIM 184756) and by liver X receptors (e.g., LXRA; MIM 602423). Upon sterol depletion, LXRs are inactive and SREBPs are cleaved, after which they bind promoter SREs and activate genes involved in cholesterol biosynthesis and uptake. Sterol transport is mediated by vesicles or by soluble protein carriers, such as steroidogenic acute regulatory protein (STAR; MIM 600617). STAR …

**Accessions** — [HGNC:18058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18058) · Entrez [134429](https://www.ncbi.nlm.nih.gov/gene/134429) · UniProt [Q96DR4](https://www.uniprot.org/uniprotkb/Q96DR4) · Ensembl [ENSG00000164211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164211)

## Data

Gene col 8903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8903); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8903]; `tensor/DDL_lfc|DDL_z.npy` [8903]; `embed/gene_vectors.npy` [8903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8903 or target_col == 8903). Every well: [[STARD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
