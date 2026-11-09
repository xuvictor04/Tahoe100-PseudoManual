---
symbol: "CUL4B"
type: "gene"
col: 8149
ensembl_id: "ENSG00000158290"
name: "cullin 4B"
location: "Xq24"
module: 29
arm: "+"
pooled_cpm: 133.41
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CUL4B

*cullin 4B* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +7.0, q 1e-09, up in 4 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 0.5 µM: 1.32× (z +4.5, q 0.001, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 1.47×, HOP62 1.44×, MIA PaCa-2 1.52×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 2.76×, A498 2.49×, NCI-H1792 2.80×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 2.76×, NCI-H1792 2.66×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (NCI-H1792 2.93×); [[Triamcinolone (drug)]] 0.05 µM in 1 line (NCI-H1792 2.62×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1792 2.60×).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.604× (z -8.1, q 4e-13, down in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.769× (z -5.9, q 4e-07, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNS]] (+0.62, fdr 1e-05), [[STAG2]] (+0.61, fdr 1e-05), [[SF3B1]] (+0.61, fdr 1e-05); moves opposite to [[PFDN2]] (-0.56, fdr 1e-05), [[SLC35E4]] (-0.56, fdr 2e-05), [[RABIF]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHRDL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8149.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 1.47×, HOP62 1.44×, MIA PaCa-2 1.52×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 2.76×, A498 2.49×, NCI-H1792 2.80×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 2.76×, NCI-H1792 2.66×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (NCI-H1792 2.93×); [[Triamcinolone (drug)]] 0.05 µM in 1 line (NCI-H1792 2.62×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1792 2.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.0 | 1e-09 | 4/49 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.9 | 2e-09 | 32/48 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.2 | 1e-07 | 31/43 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 0.001 | 30/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +4.2 | 0.003 | 25/47 (MIA PaCa-2, SNU-1, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.010 | 27/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.17 | 23/48 (SNU-423, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.604×** | -8.1 | 4e-13 | 47/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -7.9 | 1e-12 | 40/46 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.617×** | -7.7 | 3e-12 | 39/47 (Hs 766T, C32, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.769×** | -5.9 | 4e-07 | 33/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -5.5 | 5e-06 | 27/47 (AN3 CA, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.717×** | -5.3 | 1e-05 | 33/47 (Hs 766T, HEC-1-A, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -5.2 | 2e-05 | 32/47 (C32, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 2e-05 | 30/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -5.0 | 4e-05 | 29/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.723×** | -4.8 | 9e-05 | 34/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.748×** | -4.6 | 2e-04 | 34/47 (J82, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.755×** | -4.5 | 3e-04 | 25/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.757×** | -4.4 | 4e-04 | 30/47 (H4, CFPAC-1, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.595×** | -4.3 | 6e-04 | 35/47 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -4.3 | 6e-04 | 27/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.688×** | -4.3 | 7e-04 | 33/47 (SW480, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.603×** | -4.2 | 8e-04 | 32/47 (MIA PaCa-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.693×** | -4.2 | 9e-04 | 35/47 (SW48, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.611×** | -4.1 | 0.001 | 31/47 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.002 | 33/47 (NCI-H1792, J82, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.710×** | -3.9 | 0.002 | 31/48 (LS 180, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.641×** | -3.7 | 0.005 | 23/47 (SW 1271, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 104 | 8 (2 ⚠) | 1 (1 ⚠) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 2.93× (z +10.2) | [[Bortezomib (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 469 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 234 | 3 (3 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.05× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -12.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 152 | 2 (2 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +13.5) ⚠ position not correctable | [[Vinblastine (sulfate) (drug)]] 5 µM 0.471× (z -10.2) |
| [[A498 (line)]] | wt | 94.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.2) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.435× (z -9.0) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 153 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 170 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 64.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.151× (z -9.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 309 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 90.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.9) |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 332 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -9.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -10.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0336× (z -14.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 1271 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 95.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 136 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNS]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[STAG2]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SF3B1]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[IL6ST]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CAV1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CPD]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZMYM3]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 | STRING 423; ⚠ same locus (36.6 kb, same strand: neighbours can correlate without regulation) |
| [[SCARB2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[COPS8]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 | pathway: DNA Damage Recognition in GG-NER; STRING 947 |
| [[MBNL1]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFDN2]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SLC35E4]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RABIF]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[CLCF1]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ESRRA]] | -0.51 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ZNF767P-1]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SCLY]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[LSM7]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ARL8A]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.50 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[PAM16]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRDL1]] | B | CHRDL1 activity raises CUL4B's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.72× lower at baseline in the lines without CHRDL1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.4, -18.9); signed map (16.2, -35.0). **Vector** length 138, 44.5% of its response variance represented; |z| ≥ 3 in 1,440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.8 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.6 | +1.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +4.5 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.2 | +1.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.0 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -5.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | cullin 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,505,920-120,604,074 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cullins |
| Reactome | 16 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; DNA Damage Recognition in GG-NER; Dual Incision in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13620](https://www.uniprot.org/uniprotkb/Q13620) (Cullin-4B):

> Core component of multiple cullin-RING-based E3 ubiquitin-protein ligase complexes which mediate the ubiquitination and subsequent proteasomal degradation of target proteins. The functional specificity of the E3 ubiquitin-protein ligase complex depends on the variable substrate recognition subunit. CUL4B may act within the complex as a scaffold protein, contributing to catalysis through positioning of the substrate and the ubiquitin-conjugating enzyme. Plays a role as part of the E3 …

**Summary**, from NCBI Gene [8450](https://www.ncbi.nlm.nih.gov/gene/8450):

> This gene is a member of the cullin family. The encoded protein forms a complex that functions as an E3 ubiquitin ligase and catalyzes the polyubiquitination of specific protein substrates in the cell. The protein interacts with a ring finger protein, and is required for the proteolysis of several regulators of DNA replication including chromatin licensing and DNA replication factor 1 and cyclin E. Multiple transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:2555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2555) · Entrez [8450](https://www.ncbi.nlm.nih.gov/gene/8450) · UniProt [Q13620](https://www.uniprot.org/uniprotkb/Q13620) · Ensembl [ENSG00000158290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158290)

## Data

Gene col 8149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8149); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8149]; `tensor/DDL_lfc|DDL_z.npy` [8149]; `embed/gene_vectors.npy` [8149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8149 or target_col == 8149). Every well: [[CUL4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
