---
symbol: "PARP12"
type: "gene"
col: 673
ensembl_id: "ENSG00000059378"
name: "poly(ADP-ribose) polymerase family member 12"
location: "7q34"
module: 32
arm: "+"
pooled_cpm: 69.19
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 40
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 55
direction_downstream: 19
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PARP12

*poly(ADP-ribose) polymerase family member 12* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.55× (z +6.0, q 1e-06, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.297× (z -17.1, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP9]] (+0.89, fdr 7e-06), [[TRIM14]] (+0.86, fdr 7e-06), [[OAS3]] (+0.85, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 19 go from it, the strongest it → [[SAMHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +6.0 | 1e-06 | 29/45 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 1e-05 | 31/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +4.2 | 0.005 | 21/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.005 | 24/45 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.005 | 17/46 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.011 | 22/46 (SNU-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.011 | 23/46 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.051 | 18/46 (KATO III, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.051 | 20/47 (CFPAC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.055 | 21/46 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.096 | 10/46 (RPMI-7951, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.097 | 16/47 (AsPC-1, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.297×** | -17.1 | 0e+00 | 44/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.331×** | -15.0 | 0e+00 | 31/38 (SK-MEL-2, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -14.8 | 0e+00 | 42/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.353×** | -14.7 | 0e+00 | 35/46 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.510×** | -13.4 | 8e-39 | 35/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.389×** | -13.3 | 3e-38 | 41/46 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -12.1 | 1e-31 | 37/47 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.429×** | -11.0 | 2e-26 | 32/41 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.580×** | -10.8 | 2e-25 | 36/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.464×** | -10.8 | 2e-25 | 33/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.465×** | -10.8 | 2e-25 | 33/46 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.468×** | -10.7 | 6e-25 | 40/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.639×** | -8.9 | 3e-17 | 30/46 (A549, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.355×** | -7.6 | 1e-12 | 32/45 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.613×** | -6.9 | 2e-10 | 35/46 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -6.1 | 5e-08 | 27/46 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.654×** | -6.0 | 8e-08 | 29/46 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -5.3 | 4e-06 | 27/47 (A549, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 91.5 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -15.7) |
| [[A549 (line)]] | wt | 115 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -21.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.122× (z -16.5) |
| [[SNU-423 (line)]] | alt | 78.7 | 0 | 16 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.145× (z -14.8) |
| [[A-172 (line)]] | wt | 79.2 | 0 | 15 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -15.5) |
| [[LoVo (line)]] | wt | 185 | 0 | 14 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.183× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 150 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 13 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.306× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 78.1 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 12 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0464× (z -22.1) |
| [[SK-MEL-2 (line)]] | alt | 107 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.2) |
| [[A498 (line)]] | wt | 118 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 74.3 | 0 | 9 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.269× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 93.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 78.5 | 0 | 8 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.259× (z -15.2) |
| [[HS-578T (line)]] | alt | 113 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.3) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.2) |
| [[RKO (line)]] | wt | 97.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.117× (z -15.6) |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0659× (z -15.6) |
| [[Hs 766T (line)]] | wt | 92.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.414× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -15.0) |
| [[SW1417 (line)]] | alt | 111 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.522× (z -8.9) |
| [[KATO III (line)]] | alt | 64.2 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.287× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 50.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.4) |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -10.2) |
| [[SW480 (line)]] | alt | 20.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -14.5) |
| [[COLO 205 (line)]] | alt | 88.7 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.235× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 55.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -10.3) |
| [[PANC-1 (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0491× (z -9.6) |
| [[H4 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0727× (z -14.1) |
| [[SW48 (line)]] | wt | 62.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -8.7) |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP9]] | +0.89 | +0.80 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 752 |
| [[TRIM14]] | +0.86 | +0.80 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS3]] | +0.85 | +0.75 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 820 |
| [[EIF2AK2]] | +0.85 | +0.74 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 668 |
| [[SLC15A3]] | +0.85 | +0.69 / +0.89 | both halves | 7e-06 |  |
| [[SHFL]] | +0.84 | +0.80 / +0.88 | both halves | 7e-06 | STRING 522 |
| [[IFI35]] | +0.84 | +0.75 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 731 |
| [[OAS1]] | +0.84 | +0.75 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 744 |
| [[CMPK2]] | +0.83 | +0.71 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 724 |
| [[OAS2]] | +0.83 | +0.68 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 661 |
| [[TAP2]] | +0.82 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[DTX3L]] | +0.82 | +0.67 / +0.88 | both halves | 7e-06 | STRING 588 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 23, C 32. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises PARP12's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI44L]] | B | IFI44L activity raises PARP12's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without IFI44L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[CD5L]] | B | CD5L activity raises PARP12's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without CD5L | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises PARP12's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.40× lower at baseline in the lines without TRIM22 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS2]] | B | OAS2 activity raises PARP12's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.26× lower at baseline in the lines without OAS2 | 0.011 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises PARP12's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without OAS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[TYMP]] | B | TYMP activity raises PARP12's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.78× lower at baseline in the lines without TYMP | 0.014 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[EPSTI1]] | B | EPSTI1 activity raises PARP12's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without EPSTI1 | 0.017 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[LY6E-DT]] | B | LY6E-DT activity raises PARP12's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 2.88× lower at baseline in the lines without LY6E-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises PARP12's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.95× lower at baseline in the lines without GBP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[CMPK2]] | B | CMPK2 activity raises PARP12's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without CMPK2 | 0.030 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PARP12's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMHD1]] | C | PARP12's natural level strengthens SAMHD1's drug response | PARP12's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.67; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | PARP12's natural level strengthens IRF9's drug response | PARP12's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.74; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | PARP12's natural level strengthens IFIT5's drug response | PARP12's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.77; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | PARP12's natural level strengthens HELZ2's drug response | PARP12's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.77; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | PARP12's natural level strengthens PML's drug response | PARP12's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.75; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NLRC5]] | C | PARP12's natural level strengthens NLRC5's drug response | PARP12's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.52; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | PARP12's natural level strengthens CMTR1's drug response | PARP12's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.69; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | PARP12's natural level strengthens PARP10's drug response | PARP12's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.70; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | PARP12's natural level strengthens TRIM25's drug response | PARP12's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.77; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | PARP12's natural level strengthens IFIT1's drug response | PARP12's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.52; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | PARP12's natural level strengthens USP18's drug response | PARP12's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.72; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | PARP12's natural level strengthens ADAR's drug response | PARP12's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.76; direction not clear | 0.018 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 54.8); signed map (64.9, 32.8). **Vector** length 135, 48.9% of its response variance represented; |z| ≥ 3 in 1,541 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.76 to 23); *Interferon Signaling* (reactome, mean cos +0.73 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.74 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +4.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.3 | -13.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.1 | -10.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.8 | -10.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.1 | -10.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.1 | -10.7 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,023,749-140,062,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22693, PARP-12, ZC3H1, ARTD12; previously ZC3HDC1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Poly(ADP-ribose) polymerases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0J9](https://www.uniprot.org/uniprotkb/Q9H0J9) (Protein mono-ADP-ribosyltransferase PARP12):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins. Acts as an antiviral factor by cooperating with PARP11 to suppress Zika virus replication. Displays anti-alphavirus activity during IFN-gamma immune activation by directly ADP-ribosylating the alphaviral non-structural proteins nsP3 and nsP4. Acts as a component of the PRKD1-driven regulatory cascade that selectively controls a major branch of the basolateral transport pathway by catalyzing the MARylation of …

**Summary**, from NCBI Gene [64761](https://www.ncbi.nlm.nih.gov/gene/64761):

> Enables NAD+-protein mono-ADP-ribosyltransferase activity. Involved in protein auto-ADP-ribosylation and transepithelial transport. Is active in trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21919) · Entrez [64761](https://www.ncbi.nlm.nih.gov/gene/64761) · UniProt [Q9H0J9](https://www.uniprot.org/uniprotkb/Q9H0J9) · Ensembl [ENSG00000059378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059378)

## Data

Gene col 673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 673); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 673]; `tensor/DDL_lfc|DDL_z.npy` [673]; `embed/gene_vectors.npy` [673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 673 or target_col == 673). Every well: [[PARP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
