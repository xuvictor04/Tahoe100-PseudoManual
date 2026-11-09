---
symbol: "DYNLRB1"
type: "gene"
col: 4702
ensembl_id: "ENSG00000125971"
name: "dynein light chain roadblock-type 1"
location: "20q11.22"
module: 18
arm: "-"
pooled_cpm: 89.28
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DYNLRB1

*dynein light chain roadblock-type 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +9.7, q 1e-19, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.62× (z +4.6, q 5e-04, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.699× (z -4.4, q 0.007, down in 35 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.734× (z -4.2, q 0.008, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAIP2]] (+0.56, fdr 4e-05), [[TSG101]] (+0.55, fdr 1e-05), [[TAB3]] (+0.53, fdr 3e-05); moves opposite to [[ANP32B]] (-0.55, fdr 2e-05), [[DDX54]] (-0.54, fdr 2e-05), [[TCOF1]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.7 | 1e-19 | 45/49 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.4 | 2e-14 | 38/43 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +5.5 | 6e-06 | 34/45 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.62×** | +4.6 | 5e-04 | 42/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 0.002 | 34/48 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.011 | 36/47 (COLO 205, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.068 | 28/48 (COLO 205, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.28×** | +3.3 | 0.068 | 24/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.073 | 26/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.085 | 26/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.085 | 26/48 (KATO III, J82, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.25× | +3.0 | 0.11 | 25/48 (NCI-H1573, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -4.4 | 0.007 | 35/48 (A549, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -4.2 | 0.008 | 29/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.061 | 27/48 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.793× | -3.1 | 0.24 | 24/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 74.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +12.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 47.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 83.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.18× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 68.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 73.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 71.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 55.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 78.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 96.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 127 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 88.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP2]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[TSG101]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TAB3]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ATG12]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SLU7]] | +0.52 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GARRE1]] | +0.52 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[RHOC]] | +0.50 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[MAP1LC3B]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 | STRING 419 |
| [[SAP18]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | +0.49 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[CCDC90B]] | +0.49 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CCDC92]] | +0.49 | +0.48 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANP32B]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[DDX54]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TCOF1]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[UTP18]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[LRRC45]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[LSM12]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SSRP1]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[BRF1]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SCAF4]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM97]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[STX18-AS1]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[DDX11]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DYNLRB1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-16.2, -49.1); signed map (-12.0, 14.6). **Vector** length 93.6, 27.5% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.2 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -4.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain roadblock-type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,516,395-34,540,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DNLC2A, ROBLD1; previously DNCL2A |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein 2 complex subunits; Dyneins, axonemal outer arm complex subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein light chain roadblock-type family |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP97](https://www.uniprot.org/uniprotkb/Q9NP97) (Dynein light chain roadblock-type 1):

> Component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Required for structural and functional integrity of cilia (By similarity). Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function (Probable). Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and …

**Summary**, from NCBI Gene [83658](https://www.ncbi.nlm.nih.gov/gene/83658):

> This gene is a member of the roadblock dynein light chain family. The encoded cytoplasmic protein is capable of binding intermediate chain proteins, interacts with transforming growth factor-beta, and has been implicated in the regulation of actin modulating proteins. Upregulation of this gene has been associated with hepatocellular carcinomas, suggesting that this gene may be involved in tumor progression. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene …

**Accessions** — [HGNC:15468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15468) · Entrez [83658](https://www.ncbi.nlm.nih.gov/gene/83658) · UniProt [Q9NP97](https://www.uniprot.org/uniprotkb/Q9NP97) · Ensembl [ENSG00000125971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125971)

## Data

Gene col 4702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4702); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4702]; `tensor/DDL_lfc|DDL_z.npy` [4702]; `embed/gene_vectors.npy` [4702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4702 or target_col == 4702). Every well: [[DYNLRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
