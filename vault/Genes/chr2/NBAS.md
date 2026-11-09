---
symbol: "NBAS"
type: "gene"
col: 7565
ensembl_id: "ENSG00000151779"
name: "NBAS subunit of NRZ tethering complex"
location: "2p24.3"
module: 40
arm: "+"
pooled_cpm: 294.27
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# NBAS

*NBAS subunit of NRZ tethering complex* — 2p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.65× (z +7.4, q 6e-11, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.336× (z -16.5, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -10.3, q 1e-22, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLG1]] (+0.68, fdr 7e-06), [[COG5]] (+0.66, fdr 1e-05), [[DYM]] (+0.65, fdr 7e-06); moves opposite to [[PNRC2]] (-0.66, fdr 7e-06), [[SKIL]] (-0.65, fdr 1e-05), [[TRIM8]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +7.4 | 6e-11 | 46/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.5 | 1e-05 | 38/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.2 | 0.003 | 32/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.003 | 34/49 (HOP62, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.003 | 40/45 (MIA PaCa-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.006 | 31/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.031 | 30/48 (PANC-1, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.047 | 29/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.10 | 24/48 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.336×** | -16.5 | 0e+00 | 44/44 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.353×** | -16.4 | 0e+00 | 49/49 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.358×** | -15.5 | 0e+00 | 47/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.394×** | -13.5 | 2e-39 | 44/45 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -10.3 | 1e-22 | 43/49 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.545×** | -9.5 | 2e-19 | 48/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -8.5 | 2e-15 | 42/48 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.698×** | -8.0 | 1e-13 | 35/48 (C32, J82, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -7.2 | 5e-11 | 36/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.674×** | -6.2 | 4e-08 | 42/48 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -6.0 | 9e-08 | 41/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -5.9 | 2e-07 | 40/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -5.5 | 1e-06 | 31/48 (C32, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.716×** | -5.2 | 6e-06 | 34/48 (C32, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -5.0 | 2e-05 | 30/48 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -3.2 | 0.036 | 27/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.042 | 25/48 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -3.1 | 0.047 | 28/49 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.825×** | -3.0 | 0.062 | 24/48 (KATO III, SW48, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.692×** | -2.9 | 0.072 | 29/49 (C32, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.703×** | -2.9 | 0.073 | 30/48 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 851 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -34.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -17.2) |
| [[SNU-423 (line)]] | alt | 217 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -14.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.0) |
| [[A-172 (line)]] | wt | 308 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -17.5) |
| [[A498 (line)]] | wt | 291 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.7) |
| [[HS-578T (line)]] | alt | 323 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 362 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.6) |
| [[J82 (line)]] | alt | 186 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -18.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 221 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.267× (z -17.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.452× (z -10.8) |
| [[PANC-1 (line)]] | alt | 264 | 2 | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.31× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.0) |
| [[C-33 A (line)]] | alt | 274 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.8) |
| [[HOP62 (line)]] | alt | 294 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 400 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 326 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.393× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 160 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.594× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.470× (z -8.6) |
| [[SW1417 (line)]] | alt | 296 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 231 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -18.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -13.5) |
| [[A-427 (line)]] | wt | 327 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -9.7) |
| [[A549 (line)]] | wt | 387 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -17.1) |
| [[Hs 766T (line)]] | wt | 266 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.406× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 370 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 400 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.3) |
| [[HT-29 (line)]] | alt | 222 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -15.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.442× (z -8.5) |
| [[KATO III (line)]] | alt | 259 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -13.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 305 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 300 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.471× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 260 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.310× (z -13.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 336 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -9.6) |
| [[RKO (line)]] | wt | 333 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -15.3) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.553× (z -10.0) |
| [[SHP-77 (line)]] | alt | 393 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 291 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.367× (z -10.7) |
| [[SNU-1 (line)]] | wt | 470 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -19.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 259 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 379 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 246 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.478× (z -8.8) |
| [[H4 (line)]] | wt | 281 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -13.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 349 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 216 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 292 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -11.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 229 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -11.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 272 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 211 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.6) |
| [[CHP-212 (line)]] | wt | 284 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 368 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.202× (z -9.4) |
| [[COLO 205 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -9.3) ⚠ toxic |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 334 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLG1]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[COG5]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[DYM]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[BIRC6]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[HTT]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RNF216]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ATRN]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[VPS53]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[LMAN1]] | +0.63 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.63 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[SEC24D]] | +0.62 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[SEC13]] | +0.62 | +0.74 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[SKIL]] | -0.65 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[TRIM8]] | -0.59 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[RNF103]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.55 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.55 | -0.69 / -0.38 | both halves | 7e-05 |  |
| [[CDC42EP1]] | -0.55 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[PSORS1C1]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[DEDD]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ELF1]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[MAD2L1BP]] | -0.52 | -0.65 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers NBAS's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSORS1C1]] | B | PSORS1C1 activity lowers NBAS's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.15× higher at baseline in the lines without PSORS1C1 | 0.087 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.3, -21.4); signed map (-45.0, 6.6). **Vector** length 108, 50.0% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | -16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | -16.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +0.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.8 | -8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.4 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -6.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | +0.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NBAS subunit of NRZ tethering complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.3 — chr2:15,166,916-15,561,340 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAG |
| Gene groups (HGNC) | NRZ tethering complex |
| Reactome | 5 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RRP1](https://www.uniprot.org/uniprotkb/A2RRP1) (NBAS subunit of NRZ tethering complex):

> Involved in Golgi-to-endoplasmic reticulum (ER) retrograde transport; the function is proposed to depend on its association in the NRZ complex which is believed to play a role in SNARE assembly at the ER. Required for normal embryonic development (By similarity). May play a role in the nonsense-mediated decay pathway of mRNAs containing premature stop codons (By similarity).

**Summary**, from NCBI Gene [51594](https://www.ncbi.nlm.nih.gov/gene/51594):

> This gene encodes a protein with two leucine zipper domains, a ribosomal protein S14 signature domain and a Sec39 like domain. The protein is thought to be involved in Golgi-to-ER transport. Mutations in this gene are associated with short stature, optic nerve atrophy, and Pelger-Huet anomaly. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:15625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15625) · Entrez [51594](https://www.ncbi.nlm.nih.gov/gene/51594) · UniProt [A2RRP1](https://www.uniprot.org/uniprotkb/A2RRP1) · Ensembl [ENSG00000151779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151779)

## Data

Gene col 7565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7565); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7565]; `tensor/DDL_lfc|DDL_z.npy` [7565]; `embed/gene_vectors.npy` [7565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7565 or target_col == 7565). Every well: [[NBAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
