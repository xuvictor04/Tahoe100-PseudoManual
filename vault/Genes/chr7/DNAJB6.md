---
symbol: "DNAJB6"
type: "gene"
col: 2700
ensembl_id: "ENSG00000105993"
name: "DnaJ heat shock protein family (Hsp40) member B6"
location: "7q36.3"
module: 12
arm: "-"
pooled_cpm: 148.38
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DNAJB6

*DnaJ heat shock protein family (Hsp40) member B6* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.54× (z +26.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 0.5 µM: 0.823× (z -4.0, q 0.029, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSN]] (+0.59, fdr 1e-05), [[DNAH1]] (+0.57, fdr 7e-05), [[ERVK13-1]] (+0.54, fdr 6e-04); moves opposite to [[NIPSNAP2]] (-0.62, fdr 1e-05), [[C1GALT1]] (-0.62, fdr 1e-05), [[KRTCAP2]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest KDR → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.54×** | +26.0 | 0e+00 | 47/48 (C32, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.57×** | +16.3 | 0e+00 | 47/49 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.11×** | +15.3 | 0e+00 | 45/48 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +14.2 | 9e-44 | 48/48 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +13.2 | 9e-38 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +12.4 | 4e-33 | 45/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +12.2 | 2e-32 | 43/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +11.3 | 2e-27 | 45/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +11.1 | 1e-26 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +10.3 | 5e-23 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.84×** | +8.9 | 3e-17 | 44/49 (SW1417, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +8.7 | 2e-16 | 43/45 (SW1417, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +7.9 | 1e-13 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +7.4 | 4e-12 | 27/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.3 | 8e-09 | 28/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 1e-05 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 23/48 (NCI-H1792, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.003 | 20/47 (SW48, C32, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.013 | 15/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **0.823×** | -4.0 | 0.029 | 25/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **0.831×** | -3.8 | 0.029 | 22/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.853× | -3.8 | 0.029 | 18/48 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.710×** | -3.7 | 0.032 | 24/48 (SW1417, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.5 | 0.046 | 21/48 (H4, LS 180, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.723×** | -3.5 | 0.046 | 23/48 (H4, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.843× | -3.4 | 0.057 | 18/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.876× | -3.4 | 0.057 | 16/48 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.061 | 23/47 (J82, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.895× | -3.2 | 0.082 | 13/49 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.858× | -3.1 | 0.082 | 21/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.898× | -3.1 | 0.082 | 10/48 (AsPC-1, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.856× | -3.1 | 0.088 | 23/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.088 | 19/47 (HOP62, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.088 | 21/49 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.089 | 12/48 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 93.9 | 16 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.41× (z +27.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 7.38× (z +27.5) | — |
| [[PANC-1 (line)]] | alt | 210 | 10 (2 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.02× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.437× (z -12.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[C32 (line)]] | wt | 191 | 13 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +25.8) | — |
| [[SW480 (line)]] | alt | 150 | 12 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.50× (z +23.8) | — |
| [[SW1417 (line)]] | alt | 226 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 153 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.46× (z +18.0) | — |
| [[A498 (line)]] | wt | 245 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +14.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.99× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 241 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +15.3) | [[Selinexor (drug)]] 5 µM 0.503× (z -11.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 70.1 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 9.50× (z +18.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 87.5 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.06× (z +20.7) | — |
| [[NCI-H2347 (line)]] | alt | 109 | 7 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 122 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.73× (z +22.6) | — |
| [[NCI-H1792 (line)]] | alt | 136 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.19× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 142 | 6 | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +15.7) | — |
| [[RKO (line)]] | wt | 146 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +20.5) | — |
| [[SW48 (line)]] | wt | 173 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 143 | 5 | 0 | [[Auranofin (drug)]] 5 µM 4.11× (z +15.7) | — |
| [[Hs 766T (line)]] | wt | 130 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.2× (z +13.5) | [[Selinexor (drug)]] 5 µM 0.548× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 138 | 5 | 0 | [[Auranofin (drug)]] 5 µM 6.71× (z +23.5) | — |
| [[hTERT-HPNE (line)]] | wt | 84.6 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 275 | 5 | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +19.8) | — |
| [[NCI-H23 (line)]] | alt | 134 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.94× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[NCI-H1573 (line)]] | alt | 61.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 114 | 3 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 6.04× (z +16.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.25× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A-427 (line)]] | wt | 88.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +21.4) | — |
| [[BT-474 (line)]] | alt | 209 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +18.0) | — |
| [[C-33 A (line)]] | alt | 123 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.30× (z +19.3) | — |
| [[HS-578T (line)]] | alt | 87.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +11.9) | — |
| [[J82 (line)]] | alt | 159 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +12.8) | — |
| [[KATO III (line)]] | alt | 166 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 240 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +18.8) | — |
| [[A-172 (line)]] | wt | 125 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.39× (z +22.0) | — |
| [[A549 (line)]] | wt | 92.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 149 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.54× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 95.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 110 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.26× (z +14.0) | — |
| [[AN3 CA (line)]] | alt | 203 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.52× (z +15.9) | — |
| [[H4 (line)]] | wt | 162 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 113 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +14.8) | — |
| [[LoVo (line)]] | wt | 211 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 169 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 132 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 80.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.70× (z +15.9) | — |
| [[SW 1271 (line)]] | alt | 168 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.03× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSN]] | +0.59 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[DNAH1]] | +0.57 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[ERVK13-1]] | +0.54 | +0.22 / +0.58 | both halves | 6e-04 |  |
| [[PSMD2]] | +0.53 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SFXN5]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PSMB7]] | +0.52 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SH3TC2]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ATPSCKMT]] | +0.52 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[TCP1]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 | STRING 418 |
| [[LARP4B]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CTNNA1]] | +0.51 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPSNAP2]] | -0.62 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[C1GALT1]] | -0.62 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[FKBP15]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[GEMIN2]] | -0.58 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[COMMD3]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NUDCD2]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MTCH2]] | -0.54 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[WDR75]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FRA10AC1]] | -0.53 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[COQ9]] | -0.53 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ZCCHC9]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| KDR | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (16.9, -15.4); signed map (20.4, 15.9). **Vector** length 106, 35.1% of its response variance represented; |z| ≥ 3 in 1,581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.7 | +26.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | +7.0 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +12.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.1 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.9 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.6 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:157,335,381-157,417,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRJ; previously LGMD1D |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 7 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75190](https://www.uniprot.org/uniprotkb/O75190) (DnaJ homolog subfamily B member 6):

> Has a stimulatory effect on the ATPase activity of HSP70 in a dose-dependent and time-dependent manner and hence acts as a co-chaperone of HSP70. Plays an indispensable role in the organization of KRT8/KRT18 filaments. Acts as an endogenous molecular chaperone for neuronal proteins including huntingtin. Suppresses aggregation and toxicity of polyglutamine-containing, aggregation-prone proteins. Also reduces cellular toxicity and caspase-3 activity.; [Isoform B]: Isoform B but not isoform A …

**Summary**, from NCBI Gene [10049](https://www.ncbi.nlm.nih.gov/gene/10049):

> This gene encodes a member of the DNAJ protein family. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. This family member may also play a role in polyglutamine aggregation in specific neurons. Alternative splicing of this gene results in multiple transcript variants; …

**Accessions** — [HGNC:14888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14888) · Entrez [10049](https://www.ncbi.nlm.nih.gov/gene/10049) · UniProt [O75190](https://www.uniprot.org/uniprotkb/O75190) · Ensembl [ENSG00000105993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105993)

## Data

Gene col 2700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2700); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2700]; `tensor/DDL_lfc|DDL_z.npy` [2700]; `embed/gene_vectors.npy` [2700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2700 or target_col == 2700). Every well: [[DNAJB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
