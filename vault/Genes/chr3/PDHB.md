---
symbol: "PDHB"
type: "gene"
col: 9629
ensembl_id: "ENSG00000168291"
name: "pyruvate dehydrogenase E1 subunit beta"
location: "3p14.3"
module: 25
arm: "+"
pooled_cpm: 23.13
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PDHB

*pyruvate dehydrogenase E1 subunit beta* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +10.5, q 7e-23, up in 32 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.35× (z +3.7, q 0.015, up in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 4.22×, A549 5.04×, PANC-1 3.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 4.33×, SW480 2.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.657× (z -7.6, q 2e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECHS1]] (+0.63, fdr 1e-05), [[EID1]] (+0.62, fdr 7e-06), [[ALDH3A2]] (+0.61, fdr 3e-05); moves opposite to [[NRSN2-AS1]] (-0.61, fdr 2e-05), [[TAS2R4]] (-0.57, fdr 1e-04), [[TMEM269]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLTF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 4.22×, A549 5.04×, PANC-1 3.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 4.33×, SW480 2.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.16×** | +10.5 | 7e-23 | 32/44 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.97×** | +8.8 | 3e-16 | 31/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +7.0 | 6e-10 | 37/48 (J82, RKO, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.59×** | +6.3 | 3e-08 | 31/48 (J82, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.53×** | +5.4 | 9e-06 | 28/39 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.2 | 0.002 | 25/44 (NCI-H2030, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.015 | 19/46 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.30×** | +3.6 | 0.024 | 22/47 (J82, HepG2/C3A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.025 | 0/48 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.27×** | +3.3 | 0.062 | 15/45 (A-172, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.096 | 7/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.10 | 14/48 (SNU-1, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.657×** | -7.6 | 2e-11 | 28/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -7.1 | 4e-10 | 32/47 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.621×** | -6.4 | 2e-08 | 34/48 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.012 | 23/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.081 | 21/47 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.834× | -3.2 | 0.11 | 15/48 (LS 180, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -13.7) |
| [[A-427 (line)]] | wt | 31.7 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.297× (z -11.6) |
| [[PANC-1 (line)]] | alt | 23.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.7) |
| [[A549 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 1 | — | [[Oxaliplatin (drug)]] 0.05 µM 0.0586× (z -9.2) |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0592× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 19.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.5) |
| [[SW480 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHS1]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 527 |
| [[EID1]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ALDH3A2]] | +0.61 | +0.43 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[ZNF445]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[C1GALT1C1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NAA40]] | +0.57 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MAP3K4]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DLD]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 | same gene group; pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 999 |
| [[SSX2IP]] | +0.55 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[FAM98B]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MICU2]] | +0.55 | +0.52 / +0.38 | both halves | 6e-05 | pathway: Mitochondrial protein degradation |
| [[SNRNP25]] | +0.55 | +0.54 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRSN2-AS1]] | -0.61 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TAS2R4]] | -0.57 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[TMEM269]] | -0.57 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[KLRA1P]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PPP2R2D]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | -0.55 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[TRNAU1AP]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FAM184B]] | -0.54 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LINC02936]] | -0.53 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[UBAP1L]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF213-AS1]] | -0.53 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLTF]] | B | HLTF activity raises PDHB's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without HLTF | 0.081 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[HDAC6]] | B | HDAC6 activity lowers PDHB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-34.8, 19.2); signed map (-31.3, -36.3). **Vector** length 78.0, 17.0% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.8 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.4 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.2 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase E1 subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,427,630-58,433,857 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDHE1B, E1beta |
| Gene groups (HGNC) | Pyruvate dehydrogenase complex subunits; Pyruvate dehydrogenase E1 subunits |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: PDH complex synthesizes acetyl-CoA from PYR; Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P11177](https://www.uniprot.org/uniprotkb/P11177) (Pyruvate dehydrogenase E1 component subunit beta, mitochondrial):

> Together with PDHA1 forms the heterotetrameric E1 subunit of the pyruvate dehydrogenase (PDH) complex. The PDH complex catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2), and thereby links cytoplasmic glycolysis and the mitochondrial tricarboxylic acid (TCA) cycle (Probable). It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and dihydrolipoamide dehydrogenase (E3) (Probable). The E1 subunit catalyzes …

**Summary**, from NCBI Gene [5162](https://www.ncbi.nlm.nih.gov/gene/5162):

> The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and carbon dioxide, and provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle. The PDH complex is composed of multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and lipoamide dehydrogenase (E3). The E1 enzyme is a heterotetramer of two alpha …

**Accessions** — [HGNC:8808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8808) · Entrez [5162](https://www.ncbi.nlm.nih.gov/gene/5162) · UniProt [P11177](https://www.uniprot.org/uniprotkb/P11177) · Ensembl [ENSG00000168291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168291)

## Data

Gene col 9629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9629); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9629]; `tensor/DDL_lfc|DDL_z.npy` [9629]; `embed/gene_vectors.npy` [9629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9629 or target_col == 9629). Every well: [[PDHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
