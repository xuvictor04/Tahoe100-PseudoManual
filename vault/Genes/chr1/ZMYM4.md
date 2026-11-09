---
symbol: "ZMYM4"
type: "gene"
col: 7098
ensembl_id: "ENSG00000146463"
name: "zinc finger MYM-type containing 4"
location: "1p34.3"
module: 16
arm: "+"
pooled_cpm: 135.51
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZMYM4

*zinc finger MYM-type containing 4* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +12.0, q 4e-30, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.463× (z -22.4, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYRM2]] (+0.75, fdr 7e-06), [[ZNF268]] (+0.73, fdr 7e-06), [[ZNF260]] (+0.73, fdr 7e-06); moves opposite to [[IFI27L1]] (-0.68, fdr 7e-06), [[DHRS1]] (-0.66, fdr 7e-06), [[PMS2P3-1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GDAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.0 | 4e-30 | 37/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +8.7 | 8e-16 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.8 | 3e-09 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +5.4 | 7e-06 | 33/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +5.4 | 8e-06 | 38/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.16× | +4.3 | 0.001 | 18/48 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.005 | 23/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.005 | 24/47 (SW480, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.006 | 23/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.6 | 0.016 | 0/50 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +3.4 | 0.034 | 22/50 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.2 | 0.061 | 17/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 1.16× | +3.0 | 0.10 | 13/48 (HCT15, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.10 | 15/48 (SW480, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.463×** | -22.4 | 0e+00 | 49/49 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.539×** | -12.7 | 1e-34 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.544×** | -12.5 | 1e-33 | 47/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.556×** | -12.1 | 1e-31 | 48/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -11.5 | 3e-28 | 43/50 (SW 900, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -10.5 | 1e-23 | 40/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.705×** | -7.2 | 5e-11 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.704×** | -6.9 | 3e-10 | 38/47 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.740×** | -6.2 | 4e-08 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.741×** | -6.2 | 4e-08 | 39/48 (NCI-H661, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.763×** | -5.2 | 1e-05 | 26/45 (NCI-H23, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.787×** | -4.9 | 4e-05 | 29/48 (HOP62, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.789×** | -4.9 | 5e-05 | 34/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.817×** | -4.2 | 0.001 | 24/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.005 | 23/48 (HCT15, SW480, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.729×** | -3.0 | 0.097 | 19/48 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 146 | 4 | 12 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 132 | 3 | 11 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 219 | 1 | 7 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 1.91× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 175 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -25.2) |
| [[NCI-H23 (line)]] | alt | 242 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.2) |
| [[C-33 A (line)]] | alt | 256 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.9) |
| [[HT-29 (line)]] | alt | 94.5 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.2) |
| [[PANC-1 (line)]] | alt | 163 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -21.0) |
| [[RKO (line)]] | wt | 137 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 144 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -13.3) |
| [[A-172 (line)]] | wt | 95.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -20.2) |
| [[A-427 (line)]] | wt | 183 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 197 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.9) |
| [[LoVo (line)]] | wt | 134 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.54× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 155 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -17.1) |
| [[SW 900 (line)]] | alt | 128 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -18.1) |
| [[A549 (line)]] | wt | 122 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.4) |
| [[C32 (line)]] | wt | 123 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -14.2) |
| [[HOP62 (line)]] | alt | 136 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -22.6) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -21.5) |
| [[SW48 (line)]] | wt | 122 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.3) |
| [[BT-474 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.8) |
| [[COLO 205 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.5) |
| [[HCT15 (line)]] | alt | 197 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.433× (z -9.8) |
| [[LS 180 (line)]] | wt | 113 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 95.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.0) |
| [[Hs 766T (line)]] | wt | 116 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.0) |
| [[HS-578T (line)]] | alt | 142 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 79.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.5) |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.270× (z -8.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -8.5) |
| [[SHP-77 (line)]] | alt | 99.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -17.1) |
| [[SW1417 (line)]] | alt | 97.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -11.9) |
| [[A498 (line)]] | wt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.4) |
| [[AN3 CA (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -20.1) |
| [[H4 (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -13.4) |
| [[J82 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.9) |
| [[KATO III (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.356× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 143 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.7) |
| [[SW 1088 (line)]] | alt | 159 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0921× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM2]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.73 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[GDAP1]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[LZIC]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[FUNDC1]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[USP40]] | +0.72 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[ZNF480]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.72 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[RAD50]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ATRX]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI27L1]] | -0.68 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[DHRS1]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | -0.64 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[TAF5]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[STK32C]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[UBTD1]] | -0.63 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PDXP]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ANKZF1]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[PIGF]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.62 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.62 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDAP1]] | B | GDAP1 activity raises ZMYM4's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without GDAP1 | 0.061 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZMYM4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF480]] | C | ZNF480 activity raises ZMYM4's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without ZNF480 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.7, 9.0); signed map (10.8, -26.7). **Vector** length 132, 45.6% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.5 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.9 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.5 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -22.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.0 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -11.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.9 | -12.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.9 | -10.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,268,709-35,422,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0425, ZNF198L3, MYM; previously ZNF262 |
| Gene groups (HGNC) | Zinc fingers MYM-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZL5](https://www.uniprot.org/uniprotkb/Q5VZL5) (Zinc finger MYM-type protein 4):

> Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [9202](https://www.ncbi.nlm.nih.gov/gene/9202):

> Predicted to enable DNA binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13055) · Entrez [9202](https://www.ncbi.nlm.nih.gov/gene/9202) · UniProt [Q5VZL5](https://www.uniprot.org/uniprotkb/Q5VZL5) · Ensembl [ENSG00000146463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146463)

## Data

Gene col 7098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7098); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7098]; `tensor/DDL_lfc|DDL_z.npy` [7098]; `embed/gene_vectors.npy` [7098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7098 or target_col == 7098). Every well: [[ZMYM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
