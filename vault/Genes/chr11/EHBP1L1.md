---
symbol: "EHBP1L1"
type: "gene"
col: 10385
ensembl_id: "ENSG00000173442"
name: "EH domain binding protein 1 like 1"
location: "11q13.1"
module: 136
arm: "+"
pooled_cpm: 70.01
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 43
n_dd_up_clean: 1
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# EHBP1L1

*EH domain binding protein 1 like 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Peretinoin (drug)]] 0.05 µM: 1.34× (z +3.8, q 0.089, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -23.7, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCB3]] (+0.73, fdr 7e-06), [[LTBP4]] (+0.69, fdr 1e-05), [[PITPNM1]] (+0.68, fdr 7e-06); moves opposite to [[NFYC]] (-0.60, fdr 1e-05), [[THUMPD2]] (-0.60, fdr 8e-06), [[ZNF280D]] (-0.60, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.089 | 28/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Minodronic acid (drug)]] 5 µM |  | 1.52× | +3.3 | 0.30 | 18/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -23.7 | 0e+00 | 45/47 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.239×** | -21.2 | 0e+00 | 45/47 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.251×** | -19.7 | 0e+00 | 45/48 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.441×** | -12.1 | 1e-31 | 39/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.581×** | -11.3 | 9e-28 | 43/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -9.3 | 9e-19 | 41/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -8.4 | 5e-15 | 38/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -7.6 | 2e-12 | 37/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -7.4 | 1e-11 | 38/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -7.2 | 3e-11 | 32/48 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -6.8 | 4e-10 | 29/49 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -6.5 | 3e-09 | 36/47 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -6.3 | 1e-08 | 38/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -5.8 | 2e-07 | 33/48 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -5.6 | 7e-07 | 31/47 (SNU-423, CHP-212, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -5.2 | 6e-06 | 30/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.711×** | -5.0 | 2e-05 | 33/48 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -4.8 | 4e-05 | 31/48 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.551×** | -4.6 | 1e-04 | 28/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 84.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 70.5 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -17.2) |
| [[HS-578T (line)]] | alt | 83.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 77.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 96.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.3) |
| [[Hs 766T (line)]] | wt | 179 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -29.2) |
| [[NCI-H2030 (line)]] | alt | 63.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -21.6) |
| [[SNU-1 (line)]] | wt | 86.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -13.0) |
| [[A549 (line)]] | wt | 81.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.1) |
| [[H4 (line)]] | wt | 118 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -12.7) |
| [[J82 (line)]] | alt | 89.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -23.0) |
| [[KATO III (line)]] | alt | 59.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.5) |
| [[RKO (line)]] | wt | 79.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -15.5) |
| [[SNU-423 (line)]] | alt | 53.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -12.7) |
| [[A-172 (line)]] | wt | 93.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.3) |
| [[HEC-1-A (line)]] | alt | 49.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 66.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.8) |
| [[LoVo (line)]] | wt | 65.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.8) |
| [[NCI-H2347 (line)]] | alt | 86.7 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.178× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.8) |
| [[SW 900 (line)]] | alt | 76.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.2) |
| [[SW480 (line)]] | alt | 52.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -23.2) |
| [[HOP62 (line)]] | alt | 106 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -20.7) |
| [[HT-29 (line)]] | alt | 51.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.0) |
| [[LS 180 (line)]] | wt | 63.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 75.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -29.2) |
| [[SW1417 (line)]] | alt | 44.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -13.4) |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -10.0) |
| [[COLO 205 (line)]] | alt | 43.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.2) |
| [[HCT15 (line)]] | alt | 56.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -10.1) |
| [[PANC-1 (line)]] | alt | 81.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -13.7) |
| [[A-427 (line)]] | wt | 90.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -16.8) |
| [[C32 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -8.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0881× (z -8.7) |
| [[SW 1271 (line)]] | alt | 79.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0879× (z -8.7) |
| [[A498 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCB3]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[LTBP4]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[EPN1]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DPP9]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CAP1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.65 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.64 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[ARPC2]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[GDPGP1]] | +0.63 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TNK2]] | +0.63 | +0.68 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYC]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[THUMPD2]] | -0.60 | -0.57 / -0.59 | both halves | 8e-06 |  |
| [[ZNF280D]] | -0.60 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[TMEM35B]] | -0.59 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[SETD2]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[EPC1]] | -0.59 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[PHACTR2]] | -0.59 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[CHIC1]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ZBED3]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[POLR3C]] | -0.58 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARL14EP]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[RNF115]] | -0.57 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises EHBP1L1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without COL13A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[MAP2K1]] | B | MAP2K1 activity raises EHBP1L1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, -3.0); signed map (-8.6, 43.1). **Vector** length 122, 38.8% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.6 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -21.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -19.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EH domain binding protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,576,046-65,592,650 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762C186, TANGERIN |
| Gene groups (HGNC) | NT-C2 domain containing; Bivalent Mical/EHBP Rab binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3D4](https://www.uniprot.org/uniprotkb/Q8N3D4) (EH domain-binding protein 1-like protein 1):

> May act as Rab effector protein and play a role in vesicle trafficking.

**Summary**, from NCBI Gene [254102](https://www.ncbi.nlm.nih.gov/gene/254102):

> Predicted to enable actin filament binding activity and small GTPase binding activity. Predicted to be involved in actin cytoskeleton organization and endocytic recycling. Predicted to act upstream of or within several processes, including enucleation; erythrocyte differentiation; and microvillus organization. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30682) · Entrez [254102](https://www.ncbi.nlm.nih.gov/gene/254102) · UniProt [Q8N3D4](https://www.uniprot.org/uniprotkb/Q8N3D4) · Ensembl [ENSG00000173442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173442)

## Data

Gene col 10385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10385); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10385]; `tensor/DDL_lfc|DDL_z.npy` [10385]; `embed/gene_vectors.npy` [10385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10385 or target_col == 10385). Every well: [[EHBP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHBP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
