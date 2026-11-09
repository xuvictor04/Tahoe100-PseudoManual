---
symbol: "XPA"
type: "gene"
col: 5943
ensembl_id: "ENSG00000136936"
name: "XPA, DNA damage recognition and repair factor"
location: "9q22.33"
module: 198
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# XPA

*XPA, DNA damage recognition and repair factor* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.56× (z +8.6, q 4e-15, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 0.625× (z -4.8, q 8e-04, down in 18 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.680× (z -4.0, q 0.021, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0859×); [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H460 0.166×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (COLO 205 0.247×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (BT-474 0.173×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR2]] (+0.68, fdr 7e-06), [[MIER1]] (+0.68, fdr 7e-06), [[RAB9A]] (+0.67, fdr 7e-06); moves opposite to [[MAD1L1]] (-0.64, fdr 1e-05), [[FERMT3]] (-0.63, fdr 1e-05), [[PRDX1]] (-0.60, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.6 | 4e-15 | 30/47 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.3 | 7e-11 | 25/47 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.0 | 6e-10 | 26/48 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.6 | 4e-06 | 23/46 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.9 | 1e-04 | 14/36 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.8 | 1e-04 | 18/48 (RKO, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.6 | 3e-04 | 15/40 (KATO III, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 3e-04 | 17/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **1.26×** | +4.4 | 5e-04 | 19/46 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.4 | 5e-04 | 14/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 6e-04 | 18/48 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.4 | 6e-04 | 18/42 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.001 | 10/48 (J82, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.002 | 16/48 (A-427, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.020 | 11/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.3 | 0.039 | 11/48 (J82, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.065 | 7/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.065 | 4/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.065 | 10/48 (KATO III, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.065 | 11/47 (SW480, C-33 A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.069 | 11/47 (SW480, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0859×); [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H460 0.166×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (COLO 205 0.247×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (BT-474 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.625×** | -4.8 | 8e-04 | 18/41 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.680×** | -4.0 | 0.021 | 13/47 (CHP-212, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.034 | 10/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.847× | -3.3 | 0.15 | 8/47 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.173× (z -9.5) |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.166× (z -10.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0859× (z -10.7) |
| [[SW48 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR2]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[MIER1]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RAB9A]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[VAMP2]] | +0.65 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[CLK4]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[UBA3]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[FBXO9]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SNX2]] | +0.64 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD1L1]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[FERMT3]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FAM53A]] | -0.60 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ACOT7]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CHAF1B]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PABPC1L]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[EIF4A1]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.1, -3.7); signed map (-22.3, -9.5). **Vector** length 78.0, 14.7% of its response variance represented; |z| ≥ 3 in 687 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.3 | -4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | XPA, DNA damage recognition and repair factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,674,909-97,697,340 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XPAC, XP1 |
| Gene groups (HGNC) | Xeroderma pigmentosum complementation groups |
| Reactome | 8 pathways, smallest: Dual Incision in GG-NER; Formation of Incision Complex in GG-NER; Formation of TC-NER Pre-Incision Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P23025](https://www.uniprot.org/uniprotkb/P23025) (DNA repair protein complementing XP-A cells):

> Involved in DNA nucleotide excision repair (NER). Initiates repair by binding to damaged sites with various affinities, depending on the photoproduct and the transcriptional state of the region. Required for UV-induced CHEK1 phosphorylation and the recruitment of CEP164 to cyclobutane pyrimidine dimmers (CPD), sites of DNA damage after UV irradiation. During NER stimulates the 5'-3' helicase activity of XPD/ERCC2 and the DNA translocase activity of XPB/ERCC3. Connects XPD/ERCC2 and XPB/ERCC3 …

**Summary**, from NCBI Gene [7507](https://www.ncbi.nlm.nih.gov/gene/7507):

> This gene encodes a zinc finger protein plays a central role in nucleotide excision repair (NER), a specialized type of DNA repair. NER is responsible for repair of UV radiation-induced photoproducts and DNA adducts induced by chemical carcinogens and chemotherapeutic drugs. The encoded protein interacts with DNA and several NER proteins, acting as a scaffold to assemble the NER incision complex at sites of DNA damage. Mutations in this gene cause Xeroderma pigmentosum complementation group A …

**Accessions** — [HGNC:12814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12814) · Entrez [7507](https://www.ncbi.nlm.nih.gov/gene/7507) · UniProt [P23025](https://www.uniprot.org/uniprotkb/P23025) · Ensembl [ENSG00000136936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136936)

## Data

Gene col 5943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5943); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5943]; `tensor/DDL_lfc|DDL_z.npy` [5943]; `embed/gene_vectors.npy` [5943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5943 or target_col == 5943). Every well: [[XPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
