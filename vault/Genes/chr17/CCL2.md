---
symbol: "CCL2"
type: "gene"
col: 2988
ensembl_id: "ENSG00000108691"
name: "C-C motif chemokine ligand 2"
location: "17q12"
module: 14
arm: "+"
pooled_cpm: 30.68
n_lines_expressing: 16
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CCL2

*C-C motif chemokine ligand 2* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.68× (z +12.9, q 2e-35, up in 10 of 14 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 12.2× (z +12.0, q 6e-31, up in 14 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.493× (z -3.7, q 0.059, down in 8 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0184×, A498 0.132×); [[Auranofin (drug)]] 5 µM in 1 line (A498 0.123×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A498 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCL5]] (+0.68, fdr 1e-05), [[DENND2B]] (+0.66, fdr 1e-05), [[MSC]] (+0.64, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CADM1]] → it (grade B ⚠); 3 go from it, the strongest it → [[IL4I1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **5.68×** | +12.9 | 2e-35 | 10/14 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **12.2×** | +12.0 | 6e-31 | 14/14 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.71×** | +8.5 | 5e-15 | 9/11 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.89×** | +8.3 | 1e-14 | 12/13 (A-172, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.61×** | +8.0 | 1e-13 | 8/12 (A549, PANC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.23×** | +6.2 | 7e-08 | 10/14 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.88×** | +5.6 | 2e-06 | 13/14 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.88×** | +5.1 | 3e-05 | 3/11 (A549, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.38×** | +4.6 | 3e-04 | 13/14 (A-172, SW 900, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.31×** | +4.4 | 6e-04 | 10/13 (A-172, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **2.03×** | +3.7 | 0.011 | 6/13 (BT-474, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.4 | 0.034 | 4/13 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.3 | 0.041 | 6/13 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.88×** | +3.0 | 0.096 | 9/14 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0184×, A498 0.132×); [[Auranofin (drug)]] 5 µM in 1 line (A498 0.123×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A498 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.493×** | -3.7 | 0.059 | 8/13 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.494×** | -3.7 | 0.059 | 11/13 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.519× | -3.4 | 0.11 | 7/14 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.524× | -3.1 | 0.26 | 8/13 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.90 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 16.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +13.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 37.5× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 41.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +16.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 53.5× (z +14.4) | — |
| [[A-172 (line)]] | wt | 33.6 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 24.5× (z +9.4) | — |
| [[A498 (line)]] | wt | 479 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.123× (z -9.0) |
| [[HS-578T (line)]] | alt | 35.1 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 29.3× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.0184× (z -11.9) |
| [[BT-474 (line)]] | alt | 14.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 54.4× (z +15.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 64.3× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 7.74 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 48.7× (z +12.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 75.3× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 65.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 15.8× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.1× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL5]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[DENND2B]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MSC]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLC2A6]] | +0.63 | +0.57 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[VCAM1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 907 |
| [[MARCKS]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFAIP2]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IL6]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 985 |
| [[IKBKE]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CSF1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 833 |
| [[ADORA2A]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Class A/1 (Rhodopsin-like receptors); STRING 524 |
| [[CADM1]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | STRING 543 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM1]] | B | CADM1 activity raises CCL2's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without CADM1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[RASSF5]] | B | RASSF5 activity lowers CCL2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 2.18× higher at baseline in the lines without RASSF5 | 0.084 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[FRMD4A]] | C | FRMD4A activity raises CCL2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.49× lower at baseline in the lines without FRMD4A | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises CCL2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.79× lower at baseline in the lines without RRAD | 0.068 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL4I1]] | B | CCL2 activity raises IL4I1's level | lines that do not express CCL2 (34) vs lines expressing it (16) | 1.41× lower at baseline in the lines without CCL2 | 0.040 | ⚠ within organs, on part of the lines; also absent: KIRREL3, ITGA8, VCAM1 |
| [[NKX3-1]] | B | CCL2 activity raises NKX3-1's level | lines that do not express CCL2 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without CCL2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KIRREL3, ITGA8, VCAM1 |
| [[SMAD3]] | B | CCL2 activity raises SMAD3's level | lines that do not express CCL2 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without CCL2 | 0.086 | ⚠ within organs, on part of the lines; also absent: KIRREL3, ITGA8, VCAM1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 4.4); signed map (44.3, 8.8). **Vector** length 56.1, 20.5% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +1.7 | +12.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +1.7 | +8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:34,255,274-34,257,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCP1, MCP-1, MCAF, SMC-CF, GDCF-2, HC11, MGC9434; previously SCYA2 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 18 pathways, smallest: NFE2L2 regulating inflammation associated genes; Chemokine receptors bind chemokines; ATF4 activates genes in response to endoplasmic reticulum  stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P13500](https://www.uniprot.org/uniprotkb/P13500) (C-C motif chemokine 2):

> Acts as a ligand for C-C chemokine receptor CCR2. Signals through binding and activation of CCR2 and induces a strong chemotactic response and mobilization of intracellular calcium ions. Exhibits a chemotactic activity for monocytes and basophils but not neutrophils or eosinophils. May be involved in the recruitment of monocytes into the arterial wall during the disease process of atherosclerosis.

**Summary**, from NCBI Gene [6347](https://www.ncbi.nlm.nih.gov/gene/6347):

> This gene is one of several cytokine genes clustered on the q-arm of chromosome 17. Chemokines are a superfamily of secreted proteins involved in immunoregulatory and inflammatory processes. The superfamily is divided into four subfamilies based on the arrangement of N-terminal cysteine residues of the mature peptide. This chemokine is a member of the CC subfamily which is characterized by two adjacent cysteine residues. This cytokine displays chemotactic activity for monocytes and basophils …

**Accessions** — [HGNC:10618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10618) · Entrez [6347](https://www.ncbi.nlm.nih.gov/gene/6347) · UniProt [P13500](https://www.uniprot.org/uniprotkb/P13500) · Ensembl [ENSG00000108691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108691)

## Data

Gene col 2988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2988); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2988]; `tensor/DDL_lfc|DDL_z.npy` [2988]; `embed/gene_vectors.npy` [2988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2988 or target_col == 2988). Every well: [[CCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
