---
symbol: "AMIGO2"
type: "gene"
col: 6280
ensembl_id: "ENSG00000139211"
name: "adhesion molecule with Ig like domain 2"
location: "12q13.11"
module: 120
arm: "+"
pooled_cpm: 13.61
n_lines_expressing: 38
n_dd_up: 7
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 9
direction_downstream: 19
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# AMIGO2

*adhesion molecule with Ig like domain 2* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +6.5, q 5e-08, up in 14 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.89× (z +6.2, q 1e-07, up in 26 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.280× (z -12.9, q 3e-35, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCED1B]] (+0.79, fdr 7e-06, ⚠ same locus), [[ENC1]] (+0.65, fdr 7e-06), [[LINC00472]] (+0.64, fdr 1e-05), [[GPR39]] (+0.61, fdr 1e-05); moves opposite to [[ZDHHC9]] (-0.62, fdr 1e-05), [[GPR155]] (-0.55, fdr 2e-05), [[AP3S1]] (-0.53, fdr 3e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[B3GALT5]] → it (grade B ⚠); 19 go from it, the strongest it → [[ARHGAP42]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.5 | 5e-08 | 14/21 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.89×** | +6.2 | 1e-07 | 26/34 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.2 | 1e-07 | 15/30 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.8 | 3e-04 | 14/26 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.2 | 0.004 | 16/30 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.049 | 12/33 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.86×** | +3.3 | 0.079 | 11/30 (NCI-H2030, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.37× | +3.2 | 0.11 | 13/35 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.11 | 8/36 (J82, PANC-1, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.13 | 5/35 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.13 | 9/35 (A549, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.280×** | -12.9 | 3e-35 | 31/35 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.289×** | -12.5 | 1e-33 | 31/35 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.339×** | -10.9 | 2e-25 | 29/35 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -9.5 | 3e-19 | 20/34 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.443×** | -8.2 | 2e-14 | 22/35 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.537×** | -6.3 | 3e-08 | 23/35 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.545×** | -6.1 | 8e-08 | 23/35 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -6.1 | 8e-08 | 19/35 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.565×** | -5.8 | 5e-07 | 20/35 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.570×** | -5.7 | 8e-07 | 23/35 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.678×** | -5.5 | 2e-06 | 20/35 (H4, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -5.4 | 3e-06 | 20/33 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.598×** | -5.2 | 9e-06 | 16/35 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.602×** | -5.1 | 1e-05 | 17/35 (H4, NCI-H2030, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.614×** | -4.9 | 3e-05 | 18/34 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -4.6 | 1e-04 | 18/36 (A549, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 78.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0499× (z -27.3) |
| [[LoVo (line)]] | wt | 21.0 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -23.5) |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -12.8) |
| [[A549 (line)]] | wt | 62.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0509× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0931× (z -14.5) |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -14.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0907× (z -13.4) |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -10.1) |
| [[LS 180 (line)]] | wt | 6.84 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -9.3) |
| [[BT-474 (line)]] | alt | 7.90 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 7.97 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.104× (z -12.2) |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -9.8) |
| [[SW1417 (line)]] | alt | 9.89 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0587× (z -12.4) |
| [[A498 (line)]] | wt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 30.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -12.3) |
| [[HOP62 (line)]] | alt | 9.63 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.2× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 7.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0843× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.2) |
| [[SW480 (line)]] | alt | 7.30 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -8.8) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCED1B]] | +0.79 | +0.79 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ENC1]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC00472]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GPR39]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SH3RF1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CDK6]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TLR6]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NCEH1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[HTR1D]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FST]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[SERTAD4]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PLAU]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[GPR155]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[AP3S1]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[IL17RC]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[STARD9]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SEC14L2]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SCARB1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TSC22D3]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TLR2]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CD109]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LOX]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SRPX]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GALT5]] | B | B3GALT5 activity raises AMIGO2's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without B3GALT5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[RIN2]] | B | RIN2 activity raises AMIGO2's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without RIN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[LYPD1]] | B | LYPD1 activity raises AMIGO2's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without LYPD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[NRP2]] | B | NRP2 activity raises AMIGO2's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without NRP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[DUSP4]] | B | DUSP4 activity raises AMIGO2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without DUSP4 | 0.065 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[SOX9]] | B | SOX9 activity raises AMIGO2's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.85× lower at baseline in the lines without SOX9 | 0.065 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[SLC4A4]] | B | SLC4A4 activity raises AMIGO2's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without SLC4A4 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1 |
| [[NR3C1]] | B | NR3C1 activity lowers AMIGO2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PCED1B]] | C | PCED1B activity raises AMIGO2's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 5.56× lower at baseline in the lines without PCED1B | 2e-04 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP42]] | B | AMIGO2 activity raises ARHGAP42's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without AMIGO2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[RIN2]] | B | AMIGO2 activity raises RIN2's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.68× lower at baseline in the lines without AMIGO2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[SOX9]] | B | AMIGO2 activity raises SOX9's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.39× lower at baseline in the lines without AMIGO2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[TPM1]] | B | AMIGO2 activity raises TPM1's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without AMIGO2 | 0.014 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | AMIGO2 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.89× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[DUSP4]] | B | AMIGO2 activity raises DUSP4's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without AMIGO2 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[PRSS53]] | B | AMIGO2 activity lowers PRSS53's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without AMIGO2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[PTPRK]] | B | AMIGO2 activity raises PTPRK's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without AMIGO2 | 0.044 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[GPR39]] | B | AMIGO2 activity raises GPR39's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.93× lower at baseline in the lines without AMIGO2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[NRP2]] | B | AMIGO2 activity raises NRP2's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without AMIGO2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | AMIGO2 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.46× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[DOCK10]] | B | AMIGO2 activity raises DOCK10's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.99× lower at baseline in the lines without AMIGO2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.4, 13.9); signed map (15.4, 41.8). **Vector** length 99.3, 25.4% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.7 | -6.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | adhesion molecule with Ig like domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,075,707-47,079,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALI1, DEGA |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Adhesion molecule with Ig like domain family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: RAC3 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SJ2](https://www.uniprot.org/uniprotkb/Q86SJ2) (Amphoterin-induced protein 2):

> Required for depolarization-dependent survival of cultured cerebellar granule neurons. May mediate homophilic as well as heterophilic cell-cell interaction with AMIGO1 or AMIGO3. May contribute to signal transduction through its intracellular domain. May be required for tumorigenesis of a subset of gastric adenocarcinomas.

**Summary**, from NCBI Gene [347902](https://www.ncbi.nlm.nih.gov/gene/347902):

> Predicted to be involved in several processes, including heterophilic cell-cell adhesion; homophilic cell-cell adhesion; and positive regulation of synapse assembly. Predicted to be located in nucleus and plasma membrane. Predicted to be active in membrane. Biomarker of gastric adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24073) · Entrez [347902](https://www.ncbi.nlm.nih.gov/gene/347902) · UniProt [Q86SJ2](https://www.uniprot.org/uniprotkb/Q86SJ2) · Ensembl [ENSG00000139211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139211)

## Data

Gene col 6280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6280); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6280]; `tensor/DDL_lfc|DDL_z.npy` [6280]; `embed/gene_vectors.npy` [6280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6280 or target_col == 6280). Every well: [[AMIGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMIGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
