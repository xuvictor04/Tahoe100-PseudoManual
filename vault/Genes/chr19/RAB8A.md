---
symbol: "RAB8A"
type: "gene"
col: 9468
ensembl_id: "ENSG00000167461"
name: "RAB8A, member RAS oncogene family"
location: "19p13.11"
module: 7
arm: "+"
pooled_cpm: 43.47
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RAB8A

*RAB8A, member RAS oncogene family* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.40× (z +5.5, q 2e-05, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.916× (z -4.6, q 0.002, down in 3 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.762× (z -4.4, q 0.003, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP4]] (+0.62, fdr 9e-06), [[CSTF2T]] (+0.59, fdr 1e-05), [[ZBTB6]] (+0.59, fdr 1e-05); moves opposite to [[SNHG25]] (-0.60, fdr 1e-05), [[RPL36A]] (-0.60, fdr 1e-05), [[RPS24]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-05 | 32/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.37×** | +5.0 | 2e-04 | 23/39 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.34×** | +4.9 | 2e-04 | 29/46 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +4.5 | 8e-04 | 30/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.003 | 25/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.25×** | +3.6 | 0.028 | 21/46 (HT-29, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +3.5 | 0.032 | 21/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.036 | 23/48 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.036 | 22/47 (PANC-1, A549, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.088 | 21/48 (PANC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -4.6 | 0.002 | 3/49 (NCI-H661, SW 1271, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.762×** | -4.4 | 0.003 | 27/48 (SNU-423, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.3 | 0.004 | 28/48 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.007 | 26/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.019 | 27/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.072 | 22/48 (SHP-77, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -3.3 | 0.072 | 19/48 (CFPAC-1, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.823× | -3.1 | 0.16 | 18/48 (SW48, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 44.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -10.3) |
| [[A498 (line)]] | wt | 48.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | — |
| [[PANC-1 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | — |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP4]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[CSTF2T]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[VCPIP1]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[ZNF543]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZNF646]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MGAT2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NUBP1]] | +0.58 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[BBS10]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[TINF2]] | +0.57 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RBM22]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF845]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG25]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RPL36A]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[RPS24]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[RPS6]] ⚠ | -0.57 | -0.50 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NAP1L1]] | -0.55 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[RPS10]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RPS25]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RPS8]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RPL21]] ⚠ | -0.54 | -0.45 / -0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[RPS21]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RPL38]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RPL7A]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RPL22]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RAB8A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-53.5, -13.5); signed map (-0.8, -27.6). **Vector** length 87.9, 19.5% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | +5.8 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.3 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +4.9 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB8A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,111,889-16,134,234 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB8; previously MEL |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 18 pathways, smallest: VxPx cargo-targeting to cilium; TBC/RABGAPs; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61006](https://www.uniprot.org/uniprotkb/P61006) (Ras-related protein Rab-8A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB8A is involved in polarized vesicular trafficking and neurotransmitter release. Together with RAB11A, RAB3IP, the …

**Summary**, from NCBI Gene [4218](https://www.ncbi.nlm.nih.gov/gene/4218):

> The protein encoded by this gene is a member of the RAS superfamily which are small GTP/GDP-binding proteins with an average size of 200 amino acids. The RAS-related proteins of the RAB/YPT family may play a role in the transport of proteins from the endoplasmic reticulum to the Golgi and the plasma membrane. This protein shares 97%, 96%, and 51% similarity with the dog RAB8, mouse MEL, and mouse YPT1 proteins, respectively and contains the 4 GTP/GDP-binding sites that are present in all the …

**Accessions** — [HGNC:7007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7007) · Entrez [4218](https://www.ncbi.nlm.nih.gov/gene/4218) · UniProt [P61006](https://www.uniprot.org/uniprotkb/P61006) · Ensembl [ENSG00000167461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167461)

## Data

Gene col 9468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9468); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9468]; `tensor/DDL_lfc|DDL_z.npy` [9468]; `embed/gene_vectors.npy` [9468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9468 or target_col == 9468). Every well: [[RAB8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
