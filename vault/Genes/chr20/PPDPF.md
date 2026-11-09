---
symbol: "PPDPF"
type: "gene"
col: 4629
ensembl_id: "ENSG00000125534"
name: "pancreatic progenitor cell differentiation and proliferation factor"
location: "20q13.33"
module: 5
arm: "-"
pooled_cpm: 122.92
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PPDPF

*pancreatic progenitor cell differentiation and proliferation factor* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +9.8, q 8e-20, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.75× (z +5.8, q 1e-06, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.511× (z -4.6, q 0.002, down in 45 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.186×, RPMI-7951 0.323×, NCI-H2030 0.357×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF5]] (+0.63, fdr 1e-05), [[CAPN5]] (+0.63, fdr 1e-05), [[OGA]] (+0.62, fdr 3e-05); moves opposite to [[HNRNPAB]] (-0.64, fdr 1e-05), [[LETM1]] (-0.63, fdr 1e-05), [[GTPBP4]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MLF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +9.8 | 8e-20 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +8.3 | 3e-14 | 43/43 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +5.8 | 1e-06 | 41/47 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +5.6 | 3e-06 | 40/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.82×** | +4.4 | 0.001 | 41/47 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.029 | 38/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.082 | 37/47 (C-33 A, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.186×, RPMI-7951 0.323×, NCI-H2030 0.357×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.511×** | -4.6 | 0.002 | 45/46 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.655× | -3.2 | 0.44 | 41/47 (KATO III, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +10.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 69.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 213 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 157 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 297 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 63.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +10.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 125 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.78× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.94× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 65.0 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.66× (z +8.9) | — |
| [[SW480 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 69.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 60.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.09× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 228 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.3) |
| [[SW 900 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 264 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 381 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF5]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CAPN5]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[OGA]] | +0.62 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[PREPL]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SLC44A2]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ATP5IF1]] | +0.57 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[NPC2]] | +0.57 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[NGFR]] | +0.56 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[CCNG2]] | +0.56 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[ZCRB1]] | +0.55 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[GSN]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[ARRDC3]] | +0.55 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.64 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[LETM1]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PUS1]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[WDR4]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[MBD3]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TCERG1]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[BICD1]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[DDX21]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLF1]] | B | MLF1 activity raises PPDPF's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without MLF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.0, -45.0); signed map (-14.6, 6.7). **Vector** length 89.8, 37.0% of its response variance represented; |z| ≥ 3 in 604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.6 | +5.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.9 | +3.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.9 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | pancreatic progenitor cell differentiation and proliferation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,520,765-63,522,206 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ697K14.9, exdpf; previously C20orf149 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3Y8](https://www.uniprot.org/uniprotkb/Q9H3Y8) (Pancreatic progenitor cell differentiation and proliferation factor):

> Probable regulator of exocrine pancreas development.

**Summary**, from NCBI Gene [79144](https://www.ncbi.nlm.nih.gov/gene/79144):

> Predicted to be involved in cell differentiation. Predicted to act upstream of or within TORC1 signaling and liver development. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16142) · Entrez [79144](https://www.ncbi.nlm.nih.gov/gene/79144) · UniProt [Q9H3Y8](https://www.uniprot.org/uniprotkb/Q9H3Y8) · Ensembl [ENSG00000125534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125534)

## Data

Gene col 4629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4629); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4629]; `tensor/DDL_lfc|DDL_z.npy` [4629]; `embed/gene_vectors.npy` [4629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4629 or target_col == 4629). Every well: [[PPDPF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPDPF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
