---
symbol: "MAZ"
type: "gene"
col: 2373
ensembl_id: "ENSG00000103495"
name: "MYC associated zinc finger protein"
location: "16p11.2"
module: 67
arm: "+"
pooled_cpm: 29.41
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# MAZ

*MYC associated zinc finger protein* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +10.7, q 5e-24, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H1573 9.77×, SW480 4.83×, NCI-H1792 6.30×, PANC-1 3.28×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 5.19×, SW480 3.49×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.512× (z -9.2, q 3e-17, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX12]] (+0.60, fdr 7e-06), [[CARM1]] (+0.58, fdr 4e-05), [[NUMA1]] (+0.58, fdr 2e-05); moves opposite to [[SERPINB8]] (-0.57, fdr 3e-05), [[EIF3I]] (-0.56, fdr 1e-04), [[NIPAL1]] (-0.54, fdr 4e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NIPAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H1573 9.77×, SW480 4.83×, NCI-H1792 6.30×, PANC-1 3.28×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 5.19×, SW480 3.49×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +10.7 | 5e-24 | 42/43 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.6 | 2e-19 | 35/38 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +5.7 | 2e-06 | 32/41 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.77×** | +5.5 | 5e-06 | 38/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.4 | 0.001 | 27/47 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.1 | 0.16 | 4/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.38× | +3.1 | 0.16 | 17/47 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.25× | +3.0 | 0.16 | 21/48 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.25× | +3.0 | 0.16 | 20/48 (LoVo, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.512×** | -9.2 | 3e-17 | 33/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -5.5 | 9e-06 | 28/47 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.571×** | -5.4 | 1e-05 | 35/48 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -5.2 | 3e-05 | 32/48 (MIA PaCa-2, CHP-212, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.604×** | -4.9 | 1e-04 | 33/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.564×** | -4.8 | 1e-04 | 31/48 (SHP-77, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -4.0 | 0.005 | 30/48 (A498, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.751×** | -3.9 | 0.006 | 26/48 (A-427, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.687×** | -3.6 | 0.017 | 30/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -3.5 | 0.026 | 22/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.030 | 26/48 (BT-474, A498, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.679×** | -3.2 | 0.059 | 25/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -3.2 | 0.059 | 20/48 (SNU-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.059 | 20/47 (A498, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -3.1 | 0.071 | 20/48 (SK-MEL-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.694×** | -3.0 | 0.082 | 18/48 (LOX-IMVI, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -19.5) |
| [[SW480 (line)]] | alt | 26.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.2) |
| [[HOP62 (line)]] | alt | 20.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.1) |
| [[KATO III (line)]] | alt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 28.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 19.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.77× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.5) |
| [[RKO (line)]] | wt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.7) |
| [[A-172 (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.234× (z -14.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[CFPAC-1 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -8.5) |
| [[HCT15 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.22× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -11.5) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HT-29 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.4) |
| [[PANC-1 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -8.7) |
| [[A498 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX12]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CARM1]] | +0.58 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[NUMA1]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[SAMD1]] | +0.57 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RABL6]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CEP131]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ANO8]] | +0.53 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[PTMAP5]] | +0.52 | +0.56 / +0.37 | both halves | 9e-05 |  |
| [[CDCA3]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[HDGFL2]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KIF22]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 | STRING 888; ⚠ same locus (0.7 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP33]] | +0.52 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[EHMT2]] | +0.52 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB8]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[EIF3I]] | -0.56 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[NIPAL1]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LRIF1]] | -0.54 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[LACC1]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PSMD8]] | -0.50 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[ITGA2-AS1]] | -0.49 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[MYSM1]] | -0.49 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[KRT8P12]] | -0.49 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[GPATCH2L]] | -0.48 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[SLC4A10]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NOP14-AS1]] | -0.47 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPAL1]] | B | NIPAL1 activity lowers MAZ's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.55× higher at baseline in the lines without NIPAL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers MAZ's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without ZNF341-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[LACC1]] | B | LACC1 activity lowers MAZ's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.66× higher at baseline in the lines without LACC1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[SAMD11]] | B | SAMD11 activity raises MAZ's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without SAMD11 | 0.063 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[SOX12]] | B | SOX12 activity raises MAZ's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without SOX12 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |
| [[ITGA2-AS1]] | C | ITGA2-AS1 activity lowers MAZ's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ITGA2-AS1 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[NABP1]] | C | NABP1 activity lowers MAZ's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.58× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.4, -50.8); signed map (-41.0, -29.1). **Vector** length 65.0, 16.7% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.5 | +4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -1.9 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -3.6 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.5 | -4.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MYC associated zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,806,106-29,811,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZF87, Pur-1, Zif87, ZNF801 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P56270](https://www.uniprot.org/uniprotkb/P56270) (Myc-associated zinc finger protein):

> Transcriptional regulator, potentially with dual roles in transcription initiation and termination.; [Isoform 1]: Binds DNA and functions as a transcriptional activator. Binds to two G/A-rich sites, ME1a1 and ME1a2, within the MYC promoter having greater affinity for the former. Also binds to multiple G/C-rich sites within the promoter of the Sp1 family of transcription factors.; [Isoform 2]: Binds DNA and functions as a transcriptional activator. Inhibits MAZ isoform 1-mediated transcription.; …

**Summary**, from NCBI Gene [4150](https://www.ncbi.nlm.nih.gov/gene/4150):

> Enables DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in several processes, including regulation of gene expression; regulation of signal transduction; and transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6914) · Entrez [4150](https://www.ncbi.nlm.nih.gov/gene/4150) · UniProt [P56270](https://www.uniprot.org/uniprotkb/P56270) · Ensembl [ENSG00000103495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103495)

## Data

Gene col 2373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2373); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2373]; `tensor/DDL_lfc|DDL_z.npy` [2373]; `embed/gene_vectors.npy` [2373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2373 or target_col == 2373). Every well: [[MAZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
