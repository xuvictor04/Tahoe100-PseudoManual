---
symbol: "BCL6"
type: "gene"
col: 3510
ensembl_id: "ENSG00000113916"
name: "BCL6 transcription repressor"
location: "3q27.3"
module: 139
arm: "+"
pooled_cpm: 63.92
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 27
n_dd_up_clean: 41
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# BCL6

*BCL6 transcription repressor* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +12.8, q 1e-34, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.422× (z -12.0, q 1e-30, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.604× (z -9.9, q 4e-21, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF9]] (+0.73, fdr 7e-06), [[CEBPD]] (+0.71, fdr 7e-06), [[SAA2]] (+0.69, fdr 7e-06); moves opposite to [[DPP9]] (-0.49, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[JPH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 1 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +12.8 | 1e-34 | 35/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.3 | 4e-14 | 32/49 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +8.1 | 8e-14 | 33/48 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +6.1 | 1e-07 | 31/49 (C32, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.1 | 1e-07 | 29/48 (Panc 03.27, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 5e-06 | 32/49 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.46×** | +4.9 | 7e-05 | 26/47 (H4, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.43×** | +4.8 | 1e-04 | 27/49 (HOP62, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 2e-04 | 26/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 26/50 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 5e-04 | 28/49 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 7e-04 | 25/50 (A498, H4, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.002 | 23/48 (A498, HOP62, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 24/48 (H4, HOP62, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 24/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.422×** | -12.0 | 1e-30 | 37/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -11.8 | 1e-29 | 35/40 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.477×** | -10.3 | 9e-23 | 45/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.604×** | -9.9 | 4e-21 | 40/49 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -8.0 | 1e-13 | 33/48 (BT-474, HT-29, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.689×** | -7.3 | 2e-11 | 37/49 (RKO, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.862× | -7.2 | 7e-11 | 15/50 (C32, J82, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.633×** | -6.4 | 1e-08 | 38/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -6.3 | 2e-08 | 28/48 (NCI-H1573, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.424×** | -6.3 | 2e-08 | 39/48 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.689×** | -5.2 | 1e-05 | 30/49 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.493×** | -5.2 | 1e-05 | 31/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.531×** | -4.6 | 2e-04 | 29/48 (NCI-H1792, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.725×** | -4.5 | 3e-04 | 23/48 (BT-474, COLO 205, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.555×** | -4.3 | 6e-04 | 22/48 (SHP-77, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.567×** | -4.1 | 0.001 | 23/48 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.007 | 24/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.616×** | -3.5 | 0.012 | 21/48 (RKO, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.786×** | -3.3 | 0.023 | 18/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 13 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.05 µM 4.67× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.388× (z -8.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 148 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.524× (z -8.9) |
| [[A498 (line)]] | wt | 66.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 104 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 97.8 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.296× (z -9.0) |
| [[SHP-77 (line)]] | alt | 114 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.9) |
| [[SW480 (line)]] | alt | 19.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +15.6) | — |
| [[A-427 (line)]] | wt | 116 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.56× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0932× (z -16.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.158× (z -13.1) |
| [[HOP62 (line)]] | alt | 37.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 89.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.218× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 62.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +16.5) | — |
| [[LS 180 (line)]] | wt | 29.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.6) | — |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.364× (z -12.1) |
| [[A-172 (line)]] | wt | 45.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.4) | — |
| [[J82 (line)]] | alt | 74.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -16.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 79.2 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.407× (z -9.8) |
| [[SNU-423 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -13.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 71.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.48× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -9.4) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.134× (z -9.4) |
| [[H4 (line)]] | wt | 42.4 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 3.25× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 80.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.4) | — |
| [[LoVo (line)]] | wt | 56.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -9.8) |
| [[PANC-1 (line)]] | alt | 51.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 54.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.11× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +14.3) | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF9]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CEBPD]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 764 |
| [[SAA2]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SAA2-SAA4]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NAMPT]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SAA4]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[C3]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[STOM]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[SAA1]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 | pathway: Interleukin-4 and Interleukin-13 signaling |
| [[STAT3]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 903 |
| [[SOD2]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PNRC1]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH2]] | B | JPH2 activity lowers BCL6's level | lines that do not express JPH2 (19) vs lines expressing it (31) | 1.20× higher at baseline in the lines without JPH2 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL7A1, HDX, SRGN; maybe low, not absent |
| [[SLC16A7]] | B | SLC16A7 activity raises BCL6's level | lines that do not express SLC16A7 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without SLC16A7 | 0.069 | ⚠ within organs, on part of the lines; also absent: NDNF, EDIL3-DT, ZNF229 |
| [[SLC7A2]] | B | SLC7A2 activity raises BCL6's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.24× lower at baseline in the lines without SLC7A2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[PELI1]] | C | PELI1 activity strengthens BCL6's drug response | lines that do not express PELI1 (4) vs lines expressing it (46) | the lines without PELI1 respond 0.95× as strongly (z diff +0.96); strongest at Adagrasib 0.05 µM: 1.09x vs 0.85x (z diff +6.2) | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 15.9); signed map (16.6, 28.3). **Vector** length 138, 46.5% of its response variance represented; |z| ≥ 3 in 1,774 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.59 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.6 | +3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.4 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.4 | +4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.3 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.0 | -6.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.8 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | BCL6 transcription repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:187,721,377-187,745,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZBTB27, LAZ3, BCL5, BCL6A; previously ZNF51 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Hallmark sets | ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; FOXO-mediated transcription of cell death genes; TP53 Regulates Transcription of Cell Death Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P41182](https://www.uniprot.org/uniprotkb/P41182) (B-cell lymphoma 6 protein):

> Transcriptional repressor mainly required for germinal center (GC) formation and antibody affinity maturation which has different mechanisms of action specific to the lineage and biological functions. Forms complexes with different corepressors and histone deacetylases to repress the transcriptional expression of different subsets of target genes. Represses its target genes by binding directly to the DNA sequence 5'-TTCCTAGAA-3' (BCL6-binding site) or indirectly by repressing the …

**Summary**, from NCBI Gene [604](https://www.ncbi.nlm.nih.gov/gene/604):

> The protein encoded by this gene is a zinc finger transcription factor and contains an N-terminal POZ domain. This protein acts as a sequence-specific repressor of transcription, and has been shown to modulate the transcription of STAT-dependent IL-4 responses of B cells. This protein can interact with a variety of POZ-containing proteins that function as transcription corepressors. This gene is found to be frequently translocated and hypermutated in diffuse large-cell lymphoma (DLCL), and may …

**Accessions** — [HGNC:1001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1001) · Entrez [604](https://www.ncbi.nlm.nih.gov/gene/604) · UniProt [P41182](https://www.uniprot.org/uniprotkb/P41182) · Ensembl [ENSG00000113916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113916)

## Data

Gene col 3510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3510); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3510]; `tensor/DDL_lfc|DDL_z.npy` [3510]; `embed/gene_vectors.npy` [3510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3510 or target_col == 3510). Every well: [[BCL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
