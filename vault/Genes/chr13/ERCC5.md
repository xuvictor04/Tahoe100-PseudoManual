---
symbol: "ERCC5"
type: "gene"
col: 5622
ensembl_id: "ENSG00000134899"
name: "ERCC excision repair 5, endonuclease"
location: "13q33.1"
module: 41
arm: "+"
pooled_cpm: 61.84
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ERCC5

*ERCC excision repair 5, endonuclease* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +9.0, q 2e-16, up in 2 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.21× (z +4.3, q 0.004, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.475× (z -16.7, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.514× (z -14.9, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL4]] (+0.76, fdr 7e-06), [[CIR1]] (+0.72, fdr 7e-06), [[UFL1]] (+0.72, fdr 7e-06); moves opposite to [[VMA21]] (-0.57, fdr 1e-05), [[AHCY]] (-0.55, fdr 1e-05), [[ABCC1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +9.0 | 2e-16 | 2/50 (MIA PaCa-2, AsPC-1) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.004 | 20/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.005 | 18/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.005 | 14/48 (HOP62, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.037 | 15/48 (HEC-1-A, PANC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.037 | 14/46 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.047 | 9/48 (Panc 03.27, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.053 | 13/49 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -16.7 | 0e+00 | 44/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.514×** | -14.9 | 0e+00 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.504×** | -14.2 | 2e-43 | 33/43 (SW480, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -13.7 | 2e-40 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -13.4 | 4e-39 | 43/48 (RKO, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.562×** | -12.4 | 2e-33 | 28/39 (HEC-1-A, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.581×** | -12.1 | 5e-32 | 33/48 (COLO 205, SW480, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.602×** | -11.4 | 5e-28 | 42/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.677×** | -8.7 | 1e-16 | 32/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -8.1 | 3e-14 | 34/46 (Hs 766T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.711×** | -7.6 | 1e-12 | 27/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -7.5 | 3e-12 | 29/48 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -7.5 | 3e-12 | 28/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.726×** | -7.2 | 3e-11 | 27/48 (SW480, KATO III, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.582×** | -6.3 | 9e-09 | 30/48 (NCI-H1792, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.9 | 1e-07 | 27/48 (A-427, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.773×** | -5.5 | 1e-06 | 25/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.625×** | -5.5 | 1e-06 | 26/47 (A498, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -5.5 | 1e-06 | 23/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -5.1 | 1e-05 | 26/48 (Hs 766T, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -5.0 | 2e-05 | 25/48 (J82, LoVo, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.669×** | -4.7 | 6e-05 | 22/47 (A498, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.671×** | -4.7 | 7e-05 | 19/48 (CFPAC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.814×** | -4.3 | 3e-04 | 19/47 (RPMI-7951, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 114 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.306× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 36.7 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -14.3) |
| [[A498 (line)]] | wt | 110 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.485× (z -9.4) |
| [[KATO III (line)]] | alt | 93.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 72.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.9) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.3) |
| [[SW 900 (line)]] | alt | 66.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -10.0) |
| [[COLO 205 (line)]] | alt | 228 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -11.4) |
| [[HT-29 (line)]] | alt | 71.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -10.9) |
| [[HCT15 (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.355× (z -9.5) |
| [[Hs 766T (line)]] | wt | 119 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -10.3) |
| [[LS 180 (line)]] | wt | 89.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.2) ⚠ cell-cycle shift, explains ~1% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.376× (z -10.2) |
| [[A-172 (line)]] | wt | 83.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.0) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HOP62 (line)]] | alt | 42.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.388× (z -9.9) |
| [[J82 (line)]] | alt | 99.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.436× (z -9.5) |
| [[RKO (line)]] | wt | 54.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.335× (z -10.2) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 67.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.2) ⚠ cell-cycle shift, explains ~1% of this change | [[Digitoxin (drug)]] 5 µM 0.336× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.397× (z -9.0) |
| [[A-427 (line)]] | wt | 27.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.5) ⚠ cell-cycle shift, explains ~1% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.344× (z -11.6) |
| [[C32 (line)]] | wt | 57.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 59.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.364× (z -9.9) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 68.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.7) |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.350× (z -9.4) |
| [[SW48 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.253× (z -9.9) |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 38.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.338× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -8.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -13.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL4]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[CIR1]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[UFL1]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[KLC4]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ZNF451]] | +0.70 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[GOLGA5]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.69 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TMF1]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZRSR2]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[AHCY]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ABCC1]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[DPH6]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRC]] | B | SRC activity lowers ERCC5's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[POLE3]] | C | POLE3's natural level strengthens ERCC5's drug response | POLE3's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.01; direction clear | 0.050 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.2, -38.7); signed map (-12.0, 3.6). **Vector** length 122, 35.7% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +0.7 |
|  | [[NG25 (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.1 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.6 | -13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -16.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -13.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.1 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 5, endonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,845,831-102,875,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ERCM2, XPGC |
| Gene groups (HGNC) | Xeroderma pigmentosum complementation groups; ERCC excision repair associated; Rad2/XPG endonuclease family |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 7 pathways, smallest: Dual Incision in GG-NER; Formation of Incision Complex in GG-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P28715](https://www.uniprot.org/uniprotkb/P28715) (DNA excision repair protein ERCC-5):

> Single-stranded structure-specific DNA endonuclease involved in DNA excision repair. Makes the 3'incision in DNA nucleotide excision repair (NER). Binds and bends DNA repair bubble substrate and breaks base stacking at the single-strand/double-strand DNA junction of the DNA bubble. Plays a role in base excision repair (BER) by promoting the binding of DNA glycosylase NTHL1 to its substrate and increasing NTHL1 catalytic activity that removes oxidized pyrimidines from DNA. Involved in …

**Summary**, from NCBI Gene [2073](https://www.ncbi.nlm.nih.gov/gene/2073):

> This gene encodes a single-strand specific DNA endonuclease that makes the 3' incision in DNA excision repair following UV-induced damage. The protein may also function in other cellular processes, including RNA polymerase II transcription, and transcription-coupled DNA repair. Mutations in this gene cause xeroderma pigmentosum complementation group G (XP-G), which is also referred to as xeroderma pigmentosum VII (XP7), a skin disorder characterized by hypersensitivity to UV light and increased …

**Accessions** — [HGNC:3437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3437) · Entrez [2073](https://www.ncbi.nlm.nih.gov/gene/2073) · UniProt [P28715](https://www.uniprot.org/uniprotkb/P28715) · Ensembl [ENSG00000134899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134899)

## Data

Gene col 5622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5622); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5622]; `tensor/DDL_lfc|DDL_z.npy` [5622]; `embed/gene_vectors.npy` [5622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5622 or target_col == 5622). Every well: [[ERCC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
