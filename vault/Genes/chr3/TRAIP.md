---
symbol: "TRAIP"
type: "gene"
col: 11451
ensembl_id: "ENSG00000183763"
name: "TRAF interacting protein"
location: "3p21.31"
module: 71
arm: "+"
pooled_cpm: 6.61
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TRAIP

*TRAF interacting protein* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.01× (z +15.8, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.27× (z +3.4, q 0.044, up in 3 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 4.79×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 3.72×; ⚠ cell-cycle shift, explains ~36% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 3.67×; ⚠ cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.695× (z -5.0, q 2e-04, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA5]] (+0.81, fdr 7e-06), [[RAD51]] (+0.81, fdr 7e-06), [[HAUS8]] (+0.79, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11451.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 4.79×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 3.72×; ⚠ cell-cycle shift, explains ~36% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 3.67×; ⚠ cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **3.01×** | +15.8 | 0e+00 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.74×** | +14.4 | 7e-45 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.38×** | +12.4 | 3e-33 | 42/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.64×** | +6.8 | 2e-09 | 16/32 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.37×** | +6.4 | 2e-08 | 21/41 (SW480, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.51×** | +5.6 | 2e-06 | 13/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.2 | 0.002 | 11/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +4.1 | 0.002 | 11/42 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.29×** | +3.7 | 0.015 | 9/33 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.044 | 3/44 (LS 180, A-427, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.051 | 1/31 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.25×** | +3.2 | 0.066 | 10/39 (NCI-H2030, HCT15, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.25×** | +3.1 | 0.077 | 6/47 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.695×** | -5.0 | 2e-04 | 14/43 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.785×** | -5.0 | 2e-04 | 19/46 (HCT15, A-172, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.014 | 11/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.764×** | -3.9 | 0.014 | 13/43 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.080 | 8/45 (NCI-H2030, H4, …) | inconsistent across doses | low cells (technical?) |
| [[palbociclib (drug)]] 5 µM |  | 0.657× | -3.2 | 0.14 | 5/39 (SW480, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Methotrexate (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.15 | 8/43 (SW48, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +11.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 6.60 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0852× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 2.92 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0725× (z -8.7) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0594× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 3.95 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0702× (z -9.0) |
| [[A-427 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA5]] | +0.81 | +0.77 / +0.85 | both halves | 7e-06 | STRING 464 |
| [[RAD51]] | +0.81 | +0.75 / +0.83 | both halves | 7e-06 | STRING 459 |
| [[HAUS8]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[POC1A]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | STRING 447 |
| [[RECQL4]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 | STRING 446 |
| [[SPC24]] | +0.76 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[RFC4]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | STRING 401 |
| [[BLM]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[MTBP]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[POLQ]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[RFWD3]] | +0.73 | +0.68 / +0.80 | both halves | 7e-06 | same gene group |
| [[EME1]] | +0.73 | +0.65 / +0.80 | both halves | 7e-06 | STRING 494 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCC1]] | C | DSCC1 activity raises TRAIP's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without DSCC1 | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[YBX3]] | C | YBX3 activity lowers TRAIP's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.38× higher at baseline in the lines without YBX3 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.8, -48.5); signed map (-41.5, -42.0). **Vector** length 66.1, 10.1% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.0 | +15.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | +14.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.7 | +12.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | +1.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +0.9 | +1.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.9 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.9 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.8 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -5.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | TRAF interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,828,601-49,856,574 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIP, RNF206 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWF2](https://www.uniprot.org/uniprotkb/Q9BWF2) (E3 ubiquitin-protein ligase TRAIP):

> E3 ubiquitin ligase required to protect genome stability in response to replication stress. Acts as a key regulator of interstrand cross-link repair, which takes place when both strands of duplex DNA are covalently tethered together, thereby blocking replication and transcription (By similarity). Controls the choice between the two pathways of replication-coupled interstrand-cross-link repair by mediating ubiquitination of MCM7 subunit of the CMG helicase complex (By similarity). Short …

**Summary**, from NCBI Gene [10293](https://www.ncbi.nlm.nih.gov/gene/10293):

> This gene encodes a protein that contains an N-terminal RING finger motif and a putative coiled-coil domain. A similar murine protein interacts with TNFR-associated factor 1 (TRAF1), TNFR-associated factor 2 (TRAF2), and cylindromatosis. The interaction with TRAF2 inhibits TRAF2-mediated nuclear factor kappa-B, subunit 1 activation that is required for cell activation and protection against apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30764) · Entrez [10293](https://www.ncbi.nlm.nih.gov/gene/10293) · UniProt [Q9BWF2](https://www.uniprot.org/uniprotkb/Q9BWF2) · Ensembl [ENSG00000183763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183763)

## Data

Gene col 11451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11451); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11451]; `tensor/DDL_lfc|DDL_z.npy` [11451]; `embed/gene_vectors.npy` [11451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11451 or target_col == 11451). Every well: [[TRAIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
