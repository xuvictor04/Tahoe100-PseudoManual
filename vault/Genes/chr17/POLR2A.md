---
symbol: "POLR2A"
type: "gene"
col: 11175
ensembl_id: "ENSG00000181222"
name: "RNA polymerase II subunit A"
location: "17p13.1"
module: 93
arm: "+"
pooled_cpm: 305.95
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# POLR2A

*RNA polymerase II subunit A* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.81× (z +35.9, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.568× (z -7.5, q 3e-11, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.677× (z -5.4, q 2e-05, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2B]] (+0.76, fdr 7e-06), [[EMC1-AS1]] (+0.74, fdr 7e-06), [[LINC00910]] (+0.72, fdr 7e-06); moves opposite to [[AGPS]] (-0.59, fdr 1e-05), [[GFM1]] (-0.57, fdr 3e-05), [[USP14]] (-0.56, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.81×** | +35.9 | 0e+00 | 49/49 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +17.0 | 0e+00 | 49/50 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +15.6 | 0e+00 | 47/48 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +12.4 | 5e-33 | 34/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +9.2 | 3e-18 | 44/48 (J82, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +8.9 | 6e-17 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +8.2 | 1e-14 | 47/48 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 5e-11 | 35/48 (A-172, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.8 | 1e-04 | 35/48 (AsPC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.7 | 2e-04 | 28/47 (HEC-1-A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 4e-04 | 29/48 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.009 | 27/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.020 | 31/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.020 | 36/48 (NCI-H2030, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.032 | 16/49 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -7.5 | 3e-11 | 38/45 (A-427, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.677×** | -5.4 | 2e-05 | 41/48 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -4.6 | 8e-04 | 41/48 (CFPAC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.771×** | -3.7 | 0.020 | 32/48 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.767×** | -3.7 | 0.020 | 31/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.777×** | -3.6 | 0.020 | 36/48 (CFPAC-1, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.777×** | -3.6 | 0.020 | 28/48 (CFPAC-1, SW 1088, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.618×** | -3.6 | 0.020 | 31/47 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.794×** | -3.3 | 0.055 | 32/48 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.3 | 0.065 | 26/49 (SNU-423, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.656×** | -3.2 | 0.074 | 32/49 (NCI-H23, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.074 | 25/47 (NCI-H1573, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.1 | 0.083 | 21/44 (SW48, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.086 | 29/48 (CFPAC-1, C-33 A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 206 | 11 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +29.4) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 304 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +34.0) | — |
| [[KATO III (line)]] | alt | 239 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +28.1) | — |
| [[NCI-H460 (line)]] | wt | 311 | 9 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +29.4) | — |
| [[A-172 (line)]] | wt | 230 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.57× (z +31.5) | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 230 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +25.8) | — |
| [[LoVo (line)]] | wt | 249 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +29.9) | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +24.9) | — |
| [[A498 (line)]] | wt | 295 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +26.8) | — |
| [[BT-474 (line)]] | alt | 196 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +24.0) | — |
| [[LOX-IMVI (line)]] | wt | 353 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +27.6) | — |
| [[LS 180 (line)]] | wt | 242 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +25.0) | — |
| [[HEC-1-A (line)]] | alt | 197 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +29.1) | — |
| [[HOP62 (line)]] | alt | 311 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +29.6) | — |
| [[Hs 766T (line)]] | wt | 301 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.58× (z +28.6) | — |
| [[HS-578T (line)]] | alt | 206 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +30.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 339 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +29.8) | — |
| [[NCI-H23 (line)]] | alt | 655 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +18.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 258 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +22.7) | — |
| [[PANC-1 (line)]] | alt | 354 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +23.8) | — |
| [[SNU-423 (line)]] | alt | 280 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +24.5) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 482 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +26.5) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 327 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +30.3) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 546 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +24.7) | — |
| [[AN3 CA (line)]] | alt | 171 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +19.0) | — |
| [[C32 (line)]] | wt | 508 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 187 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.93× (z +25.4) | — |
| [[hTERT-HPNE (line)]] | wt | 335 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +25.2) | — |
| [[NCI-H2030 (line)]] | alt | 365 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +27.3) | — |
| [[NCI-H2347 (line)]] | alt | 185 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +22.8) | — |
| [[RPMI-7951 (line)]] | alt | 194 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +28.5) | — |
| [[SW1417 (line)]] | alt | 329 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +20.4) | — |
| [[C-33 A (line)]] | alt | 272 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +21.8) | — |
| [[COLO 205 (line)]] | alt | 344 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +21.5) | — |
| [[H4 (line)]] | wt | 182 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 227 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +20.0) | — |
| [[NCI-H1792 (line)]] | alt | 157 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +24.4) | — |
| [[RKO (line)]] | wt | 288 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +27.0) | — |
| [[A-427 (line)]] | wt | 402 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 286 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +20.5) | — |
| [[HCT15 (line)]] | alt | 454 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +22.0) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 284 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +24.7) | — |
| [[A549 (line)]] | wt | 329 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +26.5) | — |
| [[CHP-212 (line)]] | wt | 264 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +19.5) | — |
| [[NCI-H661 (line)]] | alt | 387 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 308 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +26.5) | — |
| [[SW 1088 (line)]] | alt | 387 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +11.0) | — |
| [[SW 1271 (line)]] | alt | 459 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +14.4) | — |
| [[NCI-H2122 (line)]] | alt | 400 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 346 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2B]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 999 |
| [[EMC1-AS1]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LINC00910]] | +0.72 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[KLHL15]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[NXF1]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FAM53C]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[HEXIM1]] | +0.69 | +0.54 / +0.66 | both halves | 1e-05 | STRING 705 |
| [[INTS6L]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CD27-AS1]] | +0.66 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CHCHD7]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TXNL4B]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPS]] | -0.59 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[GFM1]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[USP14]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[WDR7]] | -0.55 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[COG2]] | -0.55 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[BLMH]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[BRD7]] | -0.55 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[COA1]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NAA15]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[DDX10]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[KPNA1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 | pathway: HIV Infection |
| [[TMEM33]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLR2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.8, -25.8); signed map (3.3, 15.4). **Vector** length 142, 51.7% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +35.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +17.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.9 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.7 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.1 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.5 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.1 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -0.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,484,366-7,514,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POLRA, RPB1; previously POLR2 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P24928](https://www.uniprot.org/uniprotkb/P24928) (DNA-directed RNA polymerase II subunit RPB1):

> Catalytic core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates (By similarity). Pol II-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol II pre-initiation complex (PIC) is recruited to DNA promoters, with focused-type …

**Summary**, from NCBI Gene [5430](https://www.ncbi.nlm.nih.gov/gene/5430):

> This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, this subunit, in combination with several other polymerase subunits, forms the DNA binding domain …

**Accessions** — [HGNC:9187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9187) · Entrez [5430](https://www.ncbi.nlm.nih.gov/gene/5430) · UniProt [P24928](https://www.uniprot.org/uniprotkb/P24928) · Ensembl [ENSG00000181222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181222)

## Data

Gene col 11175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11175); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11175]; `tensor/DDL_lfc|DDL_z.npy` [11175]; `embed/gene_vectors.npy` [11175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11175 or target_col == 11175). Every well: [[POLR2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
