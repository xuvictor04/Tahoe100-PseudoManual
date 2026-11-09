---
symbol: "BID"
type: "gene"
col: 294
ensembl_id: "ENSG00000015475"
name: "BH3 interacting domain death agonist"
location: "22q11.21"
module: 14
arm: "+"
pooled_cpm: 35.38
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BID

*BH3 interacting domain death agonist* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.71× (z +8.4, q 3e-14, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.277× (z -21.1, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPR]] (+0.60, fdr 1e-05), [[TTC39C]] (+0.56, fdr 6e-05), [[LITAF]] (+0.52, fdr 5e-05); moves opposite to [[MMUT]] (-0.45, fdr 1e-04), [[ZMYM6]] (-0.45, fdr 6e-05), [[TBCCD1]] (-0.43, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SLC12A8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +8.4 | 3e-14 | 33/45 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +7.4 | 5e-11 | 32/46 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.2 | 8e-08 | 26/46 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.0 | 7e-05 | 23/45 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 7e-05 | 24/42 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.9 | 7e-05 | 18/34 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 9e-04 | 20/46 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.2 | 0.002 | 18/41 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.005 | 16/46 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.8 | 0.007 | 14/38 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.010 | 10/45 (NCI-H460, SW1417, …) | top dose only |  |
| [[Decitabine (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.11 | 11/43 (CHP-212, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.277×** | -21.1 | 0e+00 | 46/46 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.287×** | -20.6 | 0e+00 | 45/46 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.339×** | -17.8 | 0e+00 | 45/46 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.522×** | -10.7 | 2e-24 | 40/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -8.1 | 5e-14 | 27/45 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -7.7 | 1e-12 | 31/46 (SW1417, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.433×** | -7.2 | 5e-11 | 33/46 (SW1417, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -6.2 | 5e-08 | 22/45 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 1e-07 | 28/44 (J82, SW 1088, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -5.5 | 2e-06 | 27/45 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.793×** | -5.4 | 4e-06 | 25/46 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.749×** | -4.7 | 1e-04 | 22/46 (SW48, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -4.7 | 1e-04 | 21/46 (RKO, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.587×** | -4.6 | 2e-04 | 24/46 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -4.4 | 4e-04 | 20/46 (SW1417, CHP-212, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.772×** | -4.2 | 8e-04 | 18/46 (HEC-1-A, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 60.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0717× (z -21.9) |
| [[SW480 (line)]] | alt | 25.8 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.5) |
| [[SW1417 (line)]] | alt | 52.4 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -17.7) |
| [[SW48 (line)]] | wt | 47.5 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -14.7) |
| [[J82 (line)]] | alt | 36.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.199× (z -14.4) |
| [[KATO III (line)]] | alt | 29.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -14.2) |
| [[LoVo (line)]] | wt | 34.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -15.1) |
| [[BT-474 (line)]] | alt | 37.6 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -12.2) |
| [[HOP62 (line)]] | alt | 40.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -17.9) |
| [[HS-578T (line)]] | alt | 37.1 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 3.49× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 50.4 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.01× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.138× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 21.0 | 1 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.83× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -18.1) |
| [[SNU-423 (line)]] | alt | 43.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -11.6) |
| [[A-172 (line)]] | wt | 40.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.2) |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0656× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 45.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -11.1) |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0661× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.4) |
| [[A498 (line)]] | wt | 78.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -11.4) |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -10.8) |
| [[PANC-1 (line)]] | alt | 33.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.3) |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0608× (z -10.2) |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -8.9) |
| [[H4 (line)]] | wt | 38.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -9.5) |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 45.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -8.6) |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -10.1) |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.0) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPR]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[TTC39C]] | +0.56 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[LITAF]] | +0.52 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[HUNK]] | +0.49 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[SLCO2B1]] | +0.48 | +0.34 / +0.40 | both halves | 1e-04 |  |
| [[DOC2B]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SLCO3A1]] | +0.48 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[HSPA1A]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DNPEP]] | +0.47 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TRAF3]] | +0.47 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PCSK6]] | +0.47 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[SH2D4A]] | +0.46 | +0.41 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | -0.45 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[ZMYM6]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TBCCD1]] | -0.43 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[ZFP28]] | -0.41 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[C6orf89]] | -0.41 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[ZNF17]] | -0.41 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[KCTD18]] | -0.40 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TRIM52]] | -0.39 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[FAM149B1]] | -0.39 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EPOR]] | -0.39 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[UHRF2]] | -0.39 | -0.33 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A8]] | B | SLC12A8 activity raises BID's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without SLC12A8 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[IL15RA]] | B | IL15RA activity raises BID's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without IL15RA | 0.034 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[GBP3]] | B | GBP3 activity raises BID's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without GBP3 | 0.054 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[PLEKHA6]] | B | PLEKHA6 activity raises BID's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without PLEKHA6 | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SLC12A7]] | B | SLC12A7 activity raises BID's level | lines that do not express SLC12A7 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without SLC12A7 | 0.060 | ⚠ within organs, on part of the lines; also absent: LRP5, MTARC2, LYN; maybe low, not absent; its own permutation p |
| [[RRAD]] | B | RRAD activity raises BID's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.35× lower at baseline in the lines without RRAD | 0.076 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[PSMB5]] | B | PSMB5 activity lowers BID's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02605]] | B | LINC02605 activity raises BID's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without LINC02605 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.303). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 1.9); signed map (50.4, -4.6). **Vector** length 89.1, 21.7% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +8.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.7 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | BH3 interacting domain death agonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:17,734,138-17,774,770 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; BCL2 homology region 3 (BH3) only; MicroRNA protein coding host genes |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP |
| Reactome | 10 pathways, smallest: Activation, myristolyation of BID and translocation to mitochondria; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members; Activation of BAD and translocation to mitochondria |
| Matched by | ensembl_id |

**Function**, from UniProt [P55957](https://www.uniprot.org/uniprotkb/P55957) (BH3-interacting domain death agonist):

> Induces caspases and apoptosis. Counters the protective effect of BCL2 (By similarity).; [BH3-interacting domain death agonist p15]: Induces caspase activation and apoptosis. Translocates to mitochondria following cleavage and disrupts the outer mitochondrial membrane leading to the release of cytochrome c.; [Isoform 1]: Induces ICE-like proteases and apoptosis.; [Isoform 2]: Induces ICE-like proteases and apoptosis.; [Isoform 3]: Does not induce apoptosis.; [Isoform 4]: Induces ICE-like …

**Summary**, from NCBI Gene [637](https://www.ncbi.nlm.nih.gov/gene/637):

> This gene encodes a death agonist that heterodimerizes with either agonist BAX or antagonist BCL2, and thus regulate apoptosis. The encoded protein is a member of the BCL-2 family of cell death regulators. It is a mediator of mitochondrial damage induced by caspase-8 (CASP8); CASP8 cleaves this encoded protein, and the COOH-terminal part translocates to mitochondria where it triggers cytochrome c release. Multiple alternatively spliced transcript variants have been found. [provided by RefSeq, …

**Accessions** — [HGNC:1050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1050) · Entrez [637](https://www.ncbi.nlm.nih.gov/gene/637) · UniProt [P55957](https://www.uniprot.org/uniprotkb/P55957) · Ensembl [ENSG00000015475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015475)

## Data

Gene col 294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 294); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 294]; `tensor/DDL_lfc|DDL_z.npy` [294]; `embed/gene_vectors.npy` [294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 294 or target_col == 294). Every well: [[BID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
