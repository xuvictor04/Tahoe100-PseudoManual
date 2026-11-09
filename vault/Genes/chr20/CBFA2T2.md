---
symbol: "CBFA2T2"
type: "gene"
col: 1230
ensembl_id: "ENSG00000078699"
name: "CBFA2/RUNX1 partner transcriptional co-repressor 2"
location: "20q11.21-q11.22"
module: 3
arm: "+"
pooled_cpm: 250.99
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CBFA2T2

*CBFA2/RUNX1 partner transcriptional co-repressor 2* — 20q11.21-q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.64× (z +11.5, q 6e-28, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.310× (z -27.4, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.499× (z -15.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP2]] (+0.76, fdr 7e-06), [[RAB40C]] (+0.76, fdr 7e-06), [[MOSPD3]] (+0.76, fdr 7e-06); moves opposite to [[TASOR]] (-0.78, fdr 7e-06), [[ZXDB]] (-0.76, fdr 7e-06), [[KICS2]] (-0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TLR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +11.5 | 6e-28 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +8.6 | 2e-15 | 42/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +8.4 | 6e-15 | 38/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.9 | 1e-04 | 28/48 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.4 | 0.001 | 26/48 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.006 | 22/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.013 | 26/49 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.310×** | -27.4 | 0e+00 | 49/49 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.312×** | -26.2 | 0e+00 | 44/44 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.326×** | -24.2 | 0e+00 | 44/45 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -15.6 | 0e+00 | 44/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -15.6 | 0e+00 | 47/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -14.2 | 1e-43 | 47/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.657×** | -13.9 | 9e-42 | 36/48 (A549, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -9.8 | 6e-21 | 42/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -9.7 | 1e-20 | 34/48 (HOP62, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.680×** | -9.0 | 1e-17 | 41/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -7.7 | 6e-13 | 40/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -7.5 | 3e-12 | 30/48 (HOP62, A-172, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -6.6 | 2e-09 | 31/38 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -5.8 | 4e-07 | 31/48 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.777×** | -5.4 | 2e-06 | 32/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.655×** | -5.2 | 8e-06 | 28/49 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -4.1 | 0.001 | 11/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.721×** | -4.0 | 0.002 | 33/49 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -3.9 | 0.002 | 20/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.847× | -3.9 | 0.003 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.847× | -3.9 | 0.003 | 20/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.850× | -3.8 | 0.003 | 20/48 (LOX-IMVI, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 384 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.306× (z -18.0) |
| [[A-172 (line)]] | wt | 281 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.389× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 261 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.383× (z -13.5) |
| [[HT-29 (line)]] | alt | 321 | 3 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 191 | 2 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 241 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 348 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -12.6) |
| [[A-427 (line)]] | wt | 205 | 3 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 315 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -19.3) |
| [[HS-578T (line)]] | alt | 254 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -21.0) |
| [[PANC-1 (line)]] | alt | 174 | 3 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.359× (z -19.2) |
| [[J82 (line)]] | alt | 425 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -32.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.474× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 189 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.304× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 192 | 1 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.60× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.467× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.367× (z -14.6) |
| [[SNU-423 (line)]] | alt | 345 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -30.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.413× (z -12.7) |
| [[SW 900 (line)]] | alt | 229 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.419× (z -13.5) |
| [[A549 (line)]] | wt | 181 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -24.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -21.1) |
| [[KATO III (line)]] | alt | 269 | 3 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -17.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 144 | 2 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.02× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.494× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 313 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.430× (z -12.6) |
| [[SW1417 (line)]] | alt | 475 | 3 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -31.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 234 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.382× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 274 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -33.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -11.5) |
| [[SW480 (line)]] | alt | 240 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.492× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 181 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 489 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -27.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.448× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 197 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -11.9) |
| [[SW48 (line)]] | wt | 159 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0559× (z -31.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 271 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -19.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 178 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.503× (z -8.5) |
| [[BT-474 (line)]] | alt | 399 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -9.4) |
| [[H4 (line)]] | wt | 215 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -14.0) |
| [[HCT15 (line)]] | alt | 229 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -11.3) |
| [[C-33 A (line)]] | alt | 157 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -18.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 171 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.483× (z -8.8) |
| [[COLO 205 (line)]] | alt | 331 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -10.8) |
| [[LS 180 (line)]] | wt | 152 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.6) ⚠ cell-cycle shift, explains ~24% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 235 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -20.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 210 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 281 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -13.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0578× (z -33.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0849× (z -26.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 532 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -16.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0647× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 308 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | +0.76 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.76 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.76 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[GNB2]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[KCTD7]] | +0.73 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[METRN]] | +0.73 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TULP3]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.72 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.71 | +0.76 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.78 | -0.85 / -0.59 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.76 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[KICS2]] | -0.75 | -0.77 / -0.58 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.74 | -0.74 / -0.63 | both halves | 7e-06 |  |
| [[CYREN]] | -0.73 | -0.83 / -0.48 | both halves | 2e-05 |  |
| [[ZC3H4]] | -0.72 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.72 | -0.77 / -0.55 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.71 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.71 | -0.79 / -0.61 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[C9orf64]] | -0.69 | -0.77 / -0.50 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.69 | -0.73 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR4]] | B | TLR4 activity raises CBFA2T2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without TLR4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[HDAC6]] | B | HDAC6 activity lowers CBFA2T2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.1, -14.7); signed map (-33.7, 13.7). **Vector** length 144, 57.0% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +11.0 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.7 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +9.9 | +8.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -14.1 | -15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.9 | -14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -10.3 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.5 | -15.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.1 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.8 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -9.7 |

## What is on record

|  |  |
|---|---|
| Name | CBFA2/RUNX1 partner transcriptional co-repressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21-q11.22 — chr20:33,490,075-33,650,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTGR1, ZMYND3 |
| Gene groups (HGNC) | Zinc fingers MYND-type |
| Reactome | 2 pathways, smallest: Specification of primordial germ cells; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O43439](https://www.uniprot.org/uniprotkb/O43439) (Protein CBFA2T2):

> Transcriptional corepressor which facilitates transcriptional repression via its association with DNA-binding transcription factors and recruitment of other corepressors and histone-modifying enzymes. Via association with PRDM14 is involved in regulation of embryonic stem cell (ESC) pluripotency. Involved in primordial germ cell (PCG) formation. Stabilizes PRDM14 and OCT4 on chromatin in a homooligomerization-dependent manner (By similarity). Can repress the expression of MMP7 in a …

**Summary**, from NCBI Gene [9139](https://www.ncbi.nlm.nih.gov/gene/9139):

> In acute myeloid leukemia, especially in the M2 subtype, the t(8;21)(q22;q22) translocation is one of the most frequent karyotypic abnormalities. The translocation produces a chimeric gene made up of the 5'-region of the RUNX1 (AML1) gene fused to the 3'-region of the CBFA2T1 (MTG8) gene. The chimeric protein is thought to associate with the nuclear corepressor/histone deacetylase complex to block hematopoietic differentiation. The protein encoded by this gene binds to the AML1-MTG8 complex and …

**Accessions** — [HGNC:1536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1536) · Entrez [9139](https://www.ncbi.nlm.nih.gov/gene/9139) · UniProt [O43439](https://www.uniprot.org/uniprotkb/O43439) · Ensembl [ENSG00000078699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078699)

## Data

Gene col 1230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1230); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1230]; `tensor/DDL_lfc|DDL_z.npy` [1230]; `embed/gene_vectors.npy` [1230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1230 or target_col == 1230). Every well: [[CBFA2T2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBFA2T2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
