---
symbol: "SLC9A3-AS1"
type: "gene"
col: 13437
ensembl_id: "ENSG00000225138"
name: "SLC9A3 antisense RNA 1"
location: "5p15.33"
module: 157
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# SLC9A3-AS1

*SLC9A3 antisense RNA 1* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +6.1, q 6e-07, up in 18 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.34× (z +4.7, q 6e-04, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.413× (z -6.4, q 8e-08, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP410]] (+0.61, fdr 8e-06), [[GET4]] (+0.57, fdr 1e-05), [[LMNTD2]] (+0.57, fdr 1e-05); moves opposite to [[CCT6A]] (-0.47, fdr 3e-05), [[KPNA3]] (-0.46, fdr 3e-05), [[TXNDC9]] (-0.45, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[PAQR6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +6.1 | 6e-07 | 18/30 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +5.6 | 5e-06 | 13/19 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.34×** | +4.7 | 6e-04 | 25/37 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.5 | 1e-03 | 20/41 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.2 | 0.003 | 15/22 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.49×** | +4.2 | 0.003 | 22/44 (SW 900, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.04×** | +3.9 | 0.008 | 18/37 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.018 | 16/38 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.025 | 20/43 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.89×** | +3.5 | 0.025 | 14/40 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.89×** | +3.5 | 0.025 | 13/40 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.413×** | -6.4 | 8e-08 | 27/40 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.497×** | -5.4 | 2e-05 | 28/43 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.359×** | -4.1 | 0.007 | 22/39 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.685×** | -4.0 | 0.008 | 21/41 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.610×** | -3.8 | 0.016 | 20/42 (PANC-1, RKO, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -3.8 | 0.016 | 18/41 (COLO 205, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -3.7 | 0.017 | 17/43 (SNU-423, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.618×** | -3.6 | 0.019 | 21/41 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -3.4 | 0.050 | 15/42 (MIA PaCa-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.441×** | -3.3 | 0.057 | 16/29 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.675× | -3.0 | 0.13 | 15/43 (SK-MEL-2, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0589× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +10.4) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[HT-29 (line)]] | alt | 7.26 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0815× (z -9.5) |
| [[LoVo (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[RPMI-7951 (line)]] | alt | 9.48 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0485× (z -10.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[A-172 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP410]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[GET4]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LMNTD2]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DDR1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LENG8]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ISYNA1]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[KIFC2]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[IL11RA]] | +0.54 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CCNL2]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[HCN3]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RHOT2]] | +0.53 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KPNA3]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC9]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PTGES3]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[EIF2AK4]] | -0.43 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[IDE]] | -0.43 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[VWA8]] | -0.42 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[TOMM70]] | -0.42 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[DNM1L]] | -0.42 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SLC9A3-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR6]] | C | SLC9A3-AS1 activity lowers PAQR6's level | lines that do not express SLC9A3-AS1 (4) vs lines expressing it (46) | 1.62× higher at baseline in the lines without SLC9A3-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[SSPOP]] | C | SLC9A3-AS1 activity lowers SSPOP's level | lines that do not express SLC9A3-AS1 (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without SLC9A3-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.0, -24.0); signed map (0.4, 5.2). **Vector** length 73.6, 14.7% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.2 | +4.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.1 | +3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SLC9A3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.33 — chr5:473,236-480,884 (+) |
| Ensembl biotype | lncRNA |
| Also known as | UC011CLY.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40550) · Entrez [100288152](https://www.ncbi.nlm.nih.gov/gene/100288152) · Ensembl [ENSG00000225138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225138)

## Data

Gene col 13437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13437); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13437]; `tensor/DDL_lfc|DDL_z.npy` [13437]; `embed/gene_vectors.npy` [13437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13437 or target_col == 13437). Every well: [[SLC9A3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
