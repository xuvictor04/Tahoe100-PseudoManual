---
symbol: "PACS1"
type: "gene"
col: 10565
ensembl_id: "ENSG00000175115"
name: "phosphofurin acidic cluster sorting protein 1"
location: "11q13.1-q13.2"
module: 160
arm: "+"
pooled_cpm: 219.52
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# PACS1

*phosphofurin acidic cluster sorting protein 1* — 11q13.1-q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 2.18×, SHP-77 2.16×, PANC-1 1.40×, HS-578T 1.54×); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 9.07×, SNU-1 2.99×, hTERT-HPNE 2.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 2.44×, HEC-1-A 3.31×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 2.94×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.585× (z -16.0, q 0e+00, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXN]] (+0.53, fdr 7e-05), [[ZBTB46]] (+0.50, fdr 6e-05), [[C11orf80]] (+0.49, fdr 3e-05); moves opposite to [[TTC31]] (-0.48, fdr 1e-04), [[SLC35A5]] (-0.45, fdr 3e-05), [[FASTK]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SEC16B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10565.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 2.18×, SHP-77 2.16×, PANC-1 1.40×, HS-578T 1.54×); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 9.07×, SNU-1 2.99×, hTERT-HPNE 2.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 2.44×, HEC-1-A 3.31×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 2.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.9 | 0.062 | 3/48 (HepG2/C3A, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -16.0 | 0e+00 | 35/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -15.8 | 0e+00 | 29/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.615×** | -14.0 | 6e-42 | 32/45 (C32, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -13.2 | 9e-38 | 38/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -13.0 | 2e-36 | 37/48 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -12.7 | 4e-35 | 28/49 (J82, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -10.4 | 1e-23 | 39/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.717×** | -10.3 | 3e-23 | 32/49 (A-427, C32, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.718×** | -10.3 | 5e-23 | 35/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.726×** | -9.9 | 2e-21 | 29/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -8.9 | 2e-17 | 27/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.769×** | -7.9 | 2e-13 | 33/47 (SNU-1, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.787×** | -7.4 | 5e-12 | 27/48 (LS 180, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.793×** | -7.2 | 2e-11 | 26/48 (SNU-1, LS 180, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.788×** | -7.1 | 4e-11 | 27/44 (SK-MEL-2, NCI-H2030, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.683×** | -6.0 | 7e-08 | 25/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -5.8 | 3e-07 | 25/49 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -5.6 | 7e-07 | 23/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.738×** | -4.8 | 4e-05 | 25/48 (A498, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.750×** | -4.5 | 1e-04 | 23/48 (LOX-IMVI, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.752×** | -4.5 | 2e-04 | 26/49 (C32, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.872× | -4.3 | 4e-04 | 10/49 (HOP62, C32, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.840× | -3.9 | 0.002 | 19/47 (NCI-H460, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.783×** | -3.8 | 0.002 | 20/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.889× | -3.5 | 0.010 | 10/48 (NCI-H460, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 297 | 0 | 14 (9 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -19.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.273× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 310 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 271 | 0 | 12 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.385× (z -14.6) |
| [[LS 180 (line)]] | wt | 134 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 11 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -14.8) |
| [[SNU-1 (line)]] | wt | 168 | 1 (1 ⚠) | 10 (8 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -21.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.5) |
| [[A-427 (line)]] | wt | 294 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -25.0) |
| [[Panc 03.27 (line)]] | alt | 300 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -17.0) |
| [[SW480 (line)]] | alt | 197 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.376× (z -18.7) |
| [[SHP-77 (line)]] | alt | 322 | 8 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +28.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 279 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -20.1) |
| [[J82 (line)]] | alt | 387 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 175 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.395× (z -17.2) |
| [[SW1417 (line)]] | alt | 229 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -21.7) |
| [[A-172 (line)]] | wt | 233 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.588× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 216 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -10.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 211 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 286 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -18.7) |
| [[BT-474 (line)]] | alt | 319 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -11.8) |
| [[HS-578T (line)]] | alt | 198 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.6) | [[Harringtonine (drug)]] 0.5 µM 0.534× (z -10.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.559× (z -9.4) |
| [[LoVo (line)]] | wt | 156 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -14.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.441× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -10.8) |
| [[RKO (line)]] | wt | 258 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -23.4) |
| [[SNU-423 (line)]] | alt | 239 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -11.9) |
| [[A549 (line)]] | wt | 307 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -16.9) |
| [[HCT15 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HT-29 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.451× (z -12.9) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 296 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 185 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW48 (line)]] | wt | 241 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.330× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 191 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -21.8) |
| [[C-33 A (line)]] | alt | 225 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.7) |
| [[COLO 205 (line)]] | alt | 90.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 66.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.31× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 197 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[hTERT-HPNE (line)]] | wt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.1) |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.133× (z -10.6) |
| [[A498 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 322 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXN]] | +0.53 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[ZBTB46]] | +0.50 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[C11orf80]] | +0.49 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[HECTD4]] | +0.47 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[C2CD2]] | +0.47 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[AGAP1]] | +0.46 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[PTDSS2]] | +0.46 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[SNX25]] | +0.46 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[BRWD1]] | +0.45 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[RILPL1]] | +0.44 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.43 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[SLC25A29]] | +0.43 | +0.34 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC31]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SLC35A5]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FASTK]] | -0.44 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD18CP]] | -0.42 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[BCLAF1]] | -0.42 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[RRN3P1]] | -0.42 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[PIGO]] | -0.41 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TBX15]] | -0.41 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZBED8]] | -0.41 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[SEC23B]] | -0.41 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[RAB38]] | -0.41 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[EXOSC10]] | -0.41 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC16B]] | B | SEC16B activity lowers PACS1's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 1.39× higher at baseline in the lines without SEC16B | 0.035 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[PHF21B]] | B | PHF21B activity raises PACS1's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.22× lower at baseline in the lines without PHF21B | 0.037 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[SEC23B]] | C | SEC23B's natural level weakens PACS1's drug response | SEC23B's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.05; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.301). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.4, 30.8); signed map (-26.0, 23.4). **Vector** length 102, 28.4% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -10.0 | -14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.4 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | -7.3 | -7.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -6.4 | -10.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphofurin acidic cluster sorting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1-q13.2 — chr11:66,070,272-66,244,744 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10209, KIAA1175 |
| Gene groups (HGNC) | Phosphofurin acidic cluster sorting protein family |
| Reactome | 6 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VY07](https://www.uniprot.org/uniprotkb/Q6VY07) (Phosphofurin acidic cluster sorting protein 1):

> Coat protein that is involved in the localization of trans-Golgi network (TGN) membrane proteins that contain acidic cluster sorting motifs. Controls the endosome-to-Golgi trafficking of furin and mannose-6-phosphate receptor by connecting the acidic-cluster-containing cytoplasmic domain of these molecules with the adapter-protein complex-1 (AP-1) of endosomal clathrin-coated membrane pits. Involved in HIV-1 nef-mediated removal of MHC-I from the cell surface to the TGN. Required for normal ER …

**Summary**, from NCBI Gene [55690](https://www.ncbi.nlm.nih.gov/gene/55690):

> This gene encodes a protein with a putative role in the localization of trans-Golgi network (TGN) membrane proteins. Mouse and rat homologs have been identified and studies of the homologous rat protein indicate a role in directing TGN localization of furin by binding to the protease's phosphorylated cytosolic domain. In addition, the human protein plays a role in HIV-1 Nef-mediated downregulation of cell surface MHC-I molecules to the TGN, thereby enabling HIV-1 to escape immune surveillance. …

**Accessions** — [HGNC:30032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30032) · Entrez [55690](https://www.ncbi.nlm.nih.gov/gene/55690) · UniProt [Q6VY07](https://www.uniprot.org/uniprotkb/Q6VY07) · Ensembl [ENSG00000175115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175115)

## Data

Gene col 10565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10565); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10565]; `tensor/DDL_lfc|DDL_z.npy` [10565]; `embed/gene_vectors.npy` [10565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10565 or target_col == 10565). Every well: [[PACS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
