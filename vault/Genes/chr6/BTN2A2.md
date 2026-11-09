---
symbol: "BTN2A2"
type: "gene"
col: 4535
ensembl_id: "ENSG00000124508"
name: "butyrophilin subfamily 2 member A2"
location: "6p22.2"
module: 14
arm: "+"
pooled_cpm: 10.73
n_lines_expressing: 47
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BTN2A2

*butyrophilin subfamily 2 member A2* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.24× (z +41.8, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.630× (z -7.2, q 4e-10, down in 15 of 19 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.125×, SW480 0.161×, NCI-H460 0.186×, PANC-1 0.215×, …; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.180×; ⚠ unreliable plate only); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0372×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.124×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A3P-1]] (+0.74, fdr 7e-06, ⚠ same locus), [[BTN2A3P]] (+0.74, fdr 7e-06, ⚠ same locus), [[PAXIP1-AS2]] (+0.69, fdr 7e-06), [[SLC31A2]] (+0.68, fdr 7e-06), [[ZFHX2]] (+0.67, fdr 7e-06); moves opposite to [[NIPA2]] (-0.65, fdr 7e-06), [[RNPS1]] (-0.61, fdr 7e-06), [[WDR5]] (-0.61, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC2A6]] → it (grade B ⚠); 4 go from it, the strongest it → [[C7orf31]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 2 with an alert ⚠; shown: the 15 strongest. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.24×** | +41.8 | 0e+00 | 40/43 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.80×** | +24.4 | 0e+00 | 39/42 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +14.3 | 6e-44 | 28/41 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +11.1 | 1e-26 | 28/45 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.9 | 6e-21 | 31/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +8.9 | 4e-17 | 25/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.65×** | +8.0 | 7e-14 | 30/44 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +7.5 | 6e-12 | 32/44 (HT-29, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +6.9 | 3e-10 | 22/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +6.9 | 3e-10 | 20/44 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.49×** | +6.5 | 5e-09 | 21/45 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +4.8 | 6e-05 | 15/44 (SNU-423, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.6 | 2e-04 | 15/44 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 13/45 (NCI-H23, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 4/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4535.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.125×, SW480 0.161×, NCI-H460 0.186×, PANC-1 0.215×, …; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.180×; ⚠ unreliable plate only); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0372×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.124×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -7.2 | 4e-10 | 15/19 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -5.4 | 2e-05 | 18/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.776×** | -4.1 | 0.008 | 17/32 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.681× | -3.2 | 0.15 | 5/40 (NCI-H460, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.872× | -3.1 | 0.15 | 15/43 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.872× | -3.1 | 0.15 | 9/44 (A498, RPMI-7951, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.15 | 9/43 (A498, NCI-H1792, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.694× | -3.1 | 0.15 | 14/41 (SW1417, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +24.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -11.2) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 11.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +21.2) | — |
| [[A549 (line)]] | wt | 12.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +18.3) | [[AZD2858 (drug)]] 0.5 µM 0.106× (z -9.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 10.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +28.9) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.91 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +16.2) | — |
| [[J82 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +29.5) | — |
| [[NCI-H2347 (line)]] | alt | 7.14 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +15.1) | — |
| [[SNU-423 (line)]] | alt | 25.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.124× (z -9.8) |
| [[HOP62 (line)]] | alt | 7.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +16.0) | — |
| [[Hs 766T (line)]] | wt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 9.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 9.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 5.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 12.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.27× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 5.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 9.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.4) | — |
| [[HT-29 (line)]] | alt | 5.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +14.0) | — |
| [[LoVo (line)]] | wt | 6.48 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.20× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 6.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +10.4) | — |
| [[SW48 (line)]] | wt | 8.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A3P-1]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[BTN2A3P]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 | same gene group; ⚠ same locus (27.2 kb, same strand: neighbours can correlate without regulation) |
| [[PAXIP1-AS2]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[SLC31A2]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[CLK4]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[RAB29]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ARHGEF40]] | +0.64 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[FAM111A-DT]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[STAP2]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[RPS6KA6]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SLC2A6]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[GORAB]] | +0.63 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPA2]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.61 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[WDR5]] | -0.61 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[VKORC1L1]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[SETD3]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[EIF3B]] | -0.61 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[ATAD3A]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SENP5]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[FBH1]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A6]] | B | SLC2A6 activity raises BTN2A2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without SLC2A6 | 0.072 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[ANKRD33B]] | B | ANKRD33B activity raises BTN2A2's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without ANKRD33B | 0.084 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[C7orf31]] | B | C7orf31 activity raises BTN2A2's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without C7orf31 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |
| [[DNAJC18]] | C | DNAJC18 activity raises BTN2A2's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.61× lower at baseline in the lines without DNAJC18 | 0.001 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1; co-absent with the target |
| [[PER3]] | C | PER3 activity raises BTN2A2's level | lines that do not express PER3 (3) vs lines expressing it (47) | 3.60× lower at baseline in the lines without PER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: RIPOR3, PPP1R18, SYNPO2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf31]] | C | BTN2A2 activity raises C7orf31's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without BTN2A2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L; its own permutation p |
| [[ZNF182]] | C | BTN2A2 activity raises ZNF182's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without BTN2A2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L |
| [[BTN2A3P-1]] | C | BTN2A2 activity raises BTN2A3P-1's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without BTN2A2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L |
| [[BTN3A1]] | C | BTN2A2 activity raises BTN3A1's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without BTN2A2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.6, 6.5); signed map (18.0, -13.6). **Vector** length 98.7, 21.6% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +24.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +41.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +9.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 2 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,383,096-26,394,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTF2, BT2.2, BTN2.2 |
| Gene groups (HGNC) | Butyrophilins; V-set domain containing; C2-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVV5](https://www.uniprot.org/uniprotkb/Q8WVV5) (Butyrophilin subfamily 2 member A2):

> Inhibits the proliferation of CD4 and CD8 T-cells activated by anti-CD3 antibodies, T-cell metabolism and IL2 and IFNG secretion.

**Summary**, from NCBI Gene [10385](https://www.ncbi.nlm.nih.gov/gene/10385):

> Butyrophilin is the major protein associated with fat droplets in the milk. This gene is a member of the BTN2 subfamily of genes, which encode proteins belonging to the butyrophilin protein family. The gene is located in a cluster on chromosome 6, consisting of seven genes belonging to the expanding B7/butyrophilin-like group, a subset of the immunoglobulin gene superfamily. The encoded protein is a type I receptor glycoprotein involved in lipid, fatty-acid and sterol metabolism. Several …

**Accessions** — [HGNC:1137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1137) · Entrez [10385](https://www.ncbi.nlm.nih.gov/gene/10385) · UniProt [Q8WVV5](https://www.uniprot.org/uniprotkb/Q8WVV5) · Ensembl [ENSG00000124508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124508)

## Data

Gene col 4535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4535); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4535]; `tensor/DDL_lfc|DDL_z.npy` [4535]; `embed/gene_vectors.npy` [4535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4535 or target_col == 4535). Every well: [[BTN2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
