---
symbol: "SMAGP"
type: "gene"
col: 9973
ensembl_id: "ENSG00000170545"
name: "small cell adhesion glycoprotein"
location: "12q13.13"
module: 18
arm: "+"
pooled_cpm: 19.31
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SMAGP

*small cell adhesion glycoprotein* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Peretinoin (drug)]] 5 µM: 1.53× (z +6.8, q 6e-09, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -21.2, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.66, fdr 7e-06), [[GALNT14]] (+0.65, fdr 1e-05), [[FAM89A]] (+0.64, fdr 1e-05); moves opposite to [[CDKN1B]] (-0.59, fdr 1e-05), [[ECH1]] (-0.51, fdr 2e-05), [[CHD2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IL18R1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **1.53×** | +6.8 | 6e-09 | 25/45 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.5 | 1e-05 | 21/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.57×** | +5.3 | 1e-05 | 21/42 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 1e-05 | 21/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.1 | 3e-05 | 20/45 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.2 | 0.002 | 10/35 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.002 | 7/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.002 | 17/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.003 | 8/26 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +4.0 | 0.004 | 13/45 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +3.7 | 0.009 | 18/45 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +3.1 | 0.081 | 10/44 (NCI-H460, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.405×** | -21.2 | 0e+00 | 42/45 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.321×** | -18.9 | 0e+00 | 34/45 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -16.6 | 0e+00 | 38/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.458×** | -13.0 | 3e-36 | 36/45 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -7.5 | 7e-12 | 28/44 (H4, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -7.3 | 4e-11 | 22/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.652×** | -6.8 | 6e-10 | 27/44 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -6.1 | 1e-07 | 24/45 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.705×** | -5.6 | 1e-06 | 23/44 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.697×** | -5.6 | 2e-06 | 18/45 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.708×** | -5.5 | 2e-06 | 19/44 (LOX-IMVI, RKO, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.779×** | -5.2 | 1e-05 | 20/46 (RKO, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.755×** | -5.1 | 1e-05 | 19/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 1e-05 | 18/45 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -5.1 | 1e-05 | 18/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 57.6 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.4) |
| [[RKO (line)]] | wt | 88.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -25.1) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.106× (z -15.0) |
| [[COLO 205 (line)]] | alt | 67.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -18.4) |
| [[LoVo (line)]] | wt | 33.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.537× (z -14.7) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.152× (z -12.8) |
| [[SW1417 (line)]] | alt | 44.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -16.0) |
| [[A498 (line)]] | wt | 19.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -15.1) |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -11.7) |
| [[SW480 (line)]] | alt | 22.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -16.7) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -10.8) |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.652× (z -9.3) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.245× (z -8.6) |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.6) |
| [[KATO III (line)]] | alt | 20.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -10.9) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[BT-474 (line)]] | alt | 7.22 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0781× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.4) |
| [[J82 (line)]] | alt | 8.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.622× (z -8.6) ⚠ position not correctable |
| [[A549 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GALNT14]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FAM89A]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RUSC2]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NBPF9]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SIMC1]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MPP3]] | +0.57 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[VKORC1L1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.56 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CRYL1]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | -0.59 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[ECH1]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CHD2]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.48 | -0.49 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CLIP3]] | -0.48 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SKAP2]] | -0.48 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[DBP]] | -0.48 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[IFT81]] | -0.47 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CCNG2]] | -0.47 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[SF3B1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PHF21A]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL18R1]] | B | IL18R1 activity raises SMAGP's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 1.13× lower at baseline in the lines without IL18R1 | 0.079 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[ELK3]] | C | ELK3 activity raises SMAGP's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without ELK3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (21.2, -24.5); signed map (-17.6, 46.4). **Vector** length 93.7, 21.7% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.3 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +5.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -7.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -5.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.3 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | small cell adhesion glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,244,558-51,270,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC149453, MGC149454, hSMAGP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VAQ4](https://www.uniprot.org/uniprotkb/Q0VAQ4) (Small cell adhesion glycoprotein):

> May play a role in epithelial cell-cell contacts. May play a role in tumor invasiveness and metastasis formation.

**Summary**, from NCBI Gene [57228](https://www.ncbi.nlm.nih.gov/gene/57228):

> Located in cell junction and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26918) · Entrez [57228](https://www.ncbi.nlm.nih.gov/gene/57228) · UniProt [Q0VAQ4](https://www.uniprot.org/uniprotkb/Q0VAQ4) · Ensembl [ENSG00000170545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170545)

## Data

Gene col 9973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9973); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9973]; `tensor/DDL_lfc|DDL_z.npy` [9973]; `embed/gene_vectors.npy` [9973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9973 or target_col == 9973). Every well: [[SMAGP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAGP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
