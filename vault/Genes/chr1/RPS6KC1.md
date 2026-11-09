---
symbol: "RPS6KC1"
type: "gene"
col: 5886
ensembl_id: "ENSG00000136643"
name: "ribosomal protein S6 kinase C1"
location: "1q32.3"
module: 56
arm: "+"
pooled_cpm: 206.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RPS6KC1

*ribosomal protein S6 kinase C1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.75× (z +11.5, q 7e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.357× (z -23.0, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -15.7, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCYT1A]] (+0.67, fdr 7e-06), [[YKT6]] (+0.64, fdr 1e-05), [[EXOC6B]] (+0.63, fdr 1e-05); moves opposite to [[YAP1]] (-0.54, fdr 5e-05), [[ENOSF1]] (-0.54, fdr 2e-04), [[ZNF700]] (-0.53, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +11.5 | 7e-28 | 43/48 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +9.4 | 1e-18 | 34/48 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +9.2 | 7e-18 | 35/48 (C32, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +6.8 | 2e-09 | 37/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.031 | 10/48 (SW480, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.096 | 13/47 (Hs 766T, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.19 | 19/49 (C32, COLO 205, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.357×** | -23.0 | 0e+00 | 48/49 (A498, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.356×** | -22.2 | 0e+00 | 42/44 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -15.7 | 0e+00 | 41/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.552×** | -12.8 | 4e-35 | 45/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.638×** | -9.3 | 2e-18 | 34/45 (NCI-H2030, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.723×** | -7.2 | 5e-11 | 36/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -6.8 | 8e-10 | 35/50 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.729×** | -6.8 | 8e-10 | 32/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.739×** | -6.7 | 1e-09 | 34/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -6.5 | 3e-09 | 28/48 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -5.1 | 1e-05 | 24/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.807×** | -4.4 | 5e-04 | 26/47 (H4, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.885× | -3.8 | 0.006 | 5/48 (HS-578T, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -3.6 | 0.014 | 22/48 (A498, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.893× | -3.6 | 0.014 | 17/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.857× | -3.3 | 0.035 | 18/49 (A549, HOP62, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.074 | 15/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.865× | -3.0 | 0.096 | 14/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.876× | -2.9 | 0.096 | 15/48 (BT-474, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 460 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -29.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -24.8) |
| [[HS-578T (line)]] | alt | 279 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -22.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 411 | 8 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +34.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.71× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -11.9) |
| [[HOP62 (line)]] | alt | 199 | 3 | 8 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.92× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 262 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -13.2) |
| [[A-172 (line)]] | wt | 354 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -23.0) |
| [[AsPC-1 (line)]] | alt | 272 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 170 | 2 | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.91× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -18.0) |
| [[SNU-423 (line)]] | alt | 170 | 1 | 6 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.97× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -16.5) |
| [[A-427 (line)]] | wt | 151 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -25.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 126 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 166 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -16.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -15.6) |
| [[J82 (line)]] | alt | 238 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -14.7) |
| [[PANC-1 (line)]] | alt | 201 | 2 | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -9.2) |
| [[COLO 205 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +13.5) | — |
| [[H4 (line)]] | wt | 301 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 184 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -25.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 220 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.98× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 307 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.6) |
| [[SW 900 (line)]] | alt | 343 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.9) |
| [[A549 (line)]] | wt | 222 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -24.8) |
| [[HepG2_C3A (line)]] | wt | 119 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.310× (z -12.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 236 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -16.6) |
| [[SW480 (line)]] | alt | 124 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -14.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 333 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0630× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.3) |
| [[LS 180 (line)]] | wt | 110 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.73× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 210 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -19.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 231 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.43× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 316 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.6) |
| [[SW1417 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.2) |
| [[AN3 CA (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 152 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.5) |
| [[HT-29 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -11.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 148 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 1.98× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -10.1) |
| [[SNU-1 (line)]] | wt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -11.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[YKT6]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[EXOC6B]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KCTD21]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[CYB561D2]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TMEM208]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ERP44]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANKIB1]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CDRT4]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YAP1]] | -0.54 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ENOSF1]] | -0.54 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[ZNF700]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SLC16A9]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[H6PD]] | -0.51 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[MBNL3]] | -0.51 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[DDX39B]] | -0.50 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MAP3K1]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PTGR3]] | -0.50 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[SF3B3]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SINHCAF]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SLC5A6]] | -0.49 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RPS6KC1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises RPS6KC1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MBNL3]] | B | MBNL3 activity lowers RPS6KC1's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without MBNL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -29.1); signed map (-48.7, 4.8). **Vector** length 125, 44.1% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.3 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -1.7 |
|  | [[Econazole (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:213,051,233-213,274,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | humS6PKh1, RSKL1 |
| Gene groups (HGNC) | Ribosomal protein S6 kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S38](https://www.uniprot.org/uniprotkb/Q96S38) (Inactive ribosomal protein S6 kinase delta-1):

> May be involved in transmitting sphingosine-1 phosphate (SPP)-mediated signaling into the cell. Plays a role in the recruitment of PRDX3 to early endosomes.

**Summary**, from NCBI Gene [26750](https://www.ncbi.nlm.nih.gov/gene/26750):

> Sphingosine kinase catalyzes the formation of sphingosine 1 phosphate, a lipid cellular messenger. The protein encoded by this gene can bind to sphingosine kinase and to phosphatidylinositol 3-phosphate, suggesting a role in sphingosine 1 phophate signaling. The encoded protein can also bind to peroxiredoxin-3 and may help transport it to mitochondria. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:10439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10439) · Entrez [26750](https://www.ncbi.nlm.nih.gov/gene/26750) · UniProt [Q96S38](https://www.uniprot.org/uniprotkb/Q96S38) · Ensembl [ENSG00000136643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136643)

## Data

Gene col 5886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5886); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5886]; `tensor/DDL_lfc|DDL_z.npy` [5886]; `embed/gene_vectors.npy` [5886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5886 or target_col == 5886). Every well: [[RPS6KC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
