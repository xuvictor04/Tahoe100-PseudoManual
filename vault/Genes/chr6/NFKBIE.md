---
symbol: "NFKBIE"
type: "gene"
col: 7074
ensembl_id: "ENSG00000146232"
name: "NFKB inhibitor epsilon"
location: "6p21.1"
module: 14
arm: "+"
pooled_cpm: 10.23
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFKBIE

*NFKB inhibitor epsilon* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.47× (z +32.0, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.696× (z -4.0, q 0.031, down in 16 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.560× (z -3.7, q 0.070, down in 10 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.214×, CFPAC-1 0.257×, A-172 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0686×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0648×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.107×); [[Entrectinib (drug)]] 5 µM in 1 line (C32 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD82]] (+0.71, fdr 7e-06), [[IRAK2]] (+0.70, fdr 7e-06), [[CSRNP1]] (+0.69, fdr 7e-06); moves opposite to [[PDS5A]] (-0.63, fdr 1e-05), [[RPUSD4]] (-0.57, fdr 1e-05), [[AHSA1]] (-0.56, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CSF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.47×** | +32.0 | 0e+00 | 43/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.06×** | +18.9 | 0e+00 | 45/46 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.23×** | +17.5 | 0e+00 | 41/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **11.8×** | +15.6 | 0e+00 | 43/46 (Panc 03.27, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.15×** | +9.3 | 2e-18 | 33/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.08×** | +8.9 | 6e-17 | 35/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.06×** | +8.7 | 2e-16 | 30/40 (HOP62, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +8.7 | 2e-16 | 32/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.99×** | +8.3 | 4e-15 | 34/47 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.99×** | +8.3 | 4e-15 | 32/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.04×** | +8.3 | 5e-15 | 27/38 (PANC-1, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.11×** | +7.2 | 3e-11 | 25/41 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.80×** | +7.1 | 5e-11 | 26/40 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +4.8 | 6e-05 | 17/47 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.52×** | +4.7 | 1e-04 | 12/26 (SNU-423, J82, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.008 | 14/47 (SNU-1, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.016 | 14/45 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.036 | 9/48 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.040 | 2/46 (C-33 A, Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.19× | +2.9 | 0.079 | 7/48 (J82, HS-578T, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7074.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.214×, CFPAC-1 0.257×, A-172 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0686×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0648×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.107×); [[Entrectinib (drug)]] 5 µM in 1 line (C32 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.696×** | -4.0 | 0.031 | 16/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.560×** | -3.7 | 0.070 | 10/39 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.771× | -3.2 | 0.25 | 14/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.802× | -3.1 | 0.25 | 12/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.777× | -3.1 | 0.25 | 6/47 (CHP-212, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 15.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +17.0) | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -8.7) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 25.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 13.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +19.5) | — |
| [[A549 (line)]] | wt | 10.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 8.46 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +17.5) | — |
| [[HS-578T (line)]] | alt | 15.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 3.58 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +21.1) | — |
| [[C32 (line)]] | wt | 8.44 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +12.4) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.107× (z -9.3) |
| [[J82 (line)]] | alt | 13.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +19.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +11.2) | — |
| [[SW480 (line)]] | alt | 5.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 8.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +8.7) | — |
| [[H4 (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 9.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +16.0) | — |
| [[hTERT-HPNE (line)]] | wt | 9.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +13.6) | — |
| [[KATO III (line)]] | alt | 8.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +10.6) | — |
| [[LoVo (line)]] | wt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 4.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 6.16 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0686× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 9.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 9.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0648× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 9.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +12.8) | — |
| [[A-427 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD82]] | +0.71 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[IRAK2]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | STRING 457 |
| [[CSRNP1]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NR1D1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[NFKB2]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 901 |
| [[NUAK2]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[KLF10]] | +0.67 | +0.75 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IER3]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL3]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 656 |
| [[CYTH4]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MAP2K3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | -0.63 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[RPUSD4]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ECPAS]] | -0.53 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.53 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF2]] | B | CSF2 activity raises NFKBIE's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without CSF2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[LINC00973]] | B | LINC00973 activity raises NFKBIE's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without LINC00973 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[ICAM1]] | B | ICAM1 activity raises NFKBIE's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without ICAM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[CADM1]] | B | CADM1 activity raises NFKBIE's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without CADM1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[EBI3]] | B | EBI3 activity raises NFKBIE's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without EBI3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[IL23A]] | B | IL23A activity raises NFKBIE's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without IL23A | 0.071 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[LIF-AS2]] | B | LIF-AS2 activity raises NFKBIE's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without LIF-AS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[PDLIM4]] | B | PDLIM4 activity raises NFKBIE's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without PDLIM4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[ADGRG1]] | B | ADGRG1 activity strengthens NFKBIE's drug response | lines that do not express ADGRG1 (12) vs lines expressing it (36) | the lines without ADGRG1 respond 0.80× as strongly (z diff +0.75); strongest at Homoharringtonine 0.5 µM: 2.67x vs 4.42x (z diff +2.1) | 0.089 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526; target measured in part of the lines; both ways; artifact flags |
| [[PINLYP]] | B | PINLYP activity raises NFKBIE's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.50× lower at baseline in the lines without PINLYP | 0.090 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.4, 0.8); signed map (8.4, 28.9). **Vector** length 80.1, 16.4% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.53 to 12); *TNFR2 non-canonical NF-kB pathway* (reactome, mean cos +0.50 to 9); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +18.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +32.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +0.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +0.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -0.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,258,166-44,265,788 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKBE |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NFKB inhibitor family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Activation of NF-kappaB in B cells; Downstream signaling events of B Cell Receptor (BCR); Signaling by the B Cell Receptor (BCR) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00221](https://www.uniprot.org/uniprotkb/O00221) (NF-kappa-B inhibitor epsilon):

> Sequesters NF-kappa-B transcription factor complexes in the cytoplasm, thereby inhibiting their activity. Sequestered complexes include NFKB1-RELA (p50-p65) and NFKB1-REL (p50-c-Rel) complexes. Limits B-cell activation in response to pathogens, and also plays an important role in B-cell development (By similarity).

**Summary**, from NCBI Gene [4794](https://www.ncbi.nlm.nih.gov/gene/4794):

> The protein encoded by this gene binds to components of NF-kappa-B, trapping the complex in the cytoplasm and preventing it from activating genes in the nucleus. Phosphorylation of the encoded protein targets it for destruction by the ubiquitin pathway, which activates NF-kappa-B by making it available to translocate to the nucleus. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:7799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7799) · Entrez [4794](https://www.ncbi.nlm.nih.gov/gene/4794) · UniProt [O00221](https://www.uniprot.org/uniprotkb/O00221) · Ensembl [ENSG00000146232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146232)

## Data

Gene col 7074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7074); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7074]; `tensor/DDL_lfc|DDL_z.npy` [7074]; `embed/gene_vectors.npy` [7074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7074 or target_col == 7074). Every well: [[NFKBIE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBIE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
