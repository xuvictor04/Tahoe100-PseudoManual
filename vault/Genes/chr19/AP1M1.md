---
symbol: "AP1M1"
type: "gene"
col: 1039
ensembl_id: "ENSG00000072958"
name: "adaptor related protein complex 1 subunit mu 1"
location: "19p13.11"
module: 2
arm: "+"
pooled_cpm: 29.83
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# AP1M1

*adaptor related protein complex 1 subunit mu 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.28× (z +3.9, q 0.054, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -14.8, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP9]] (+0.68, fdr 9e-06), [[MIER2]] (+0.67, fdr 1e-05), [[YKT6]] (+0.66, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.62, fdr 2e-05), [[CXCL3]] (-0.60, fdr 1e-05), [[TFAP2A-AS1]] (-0.60, fdr 7e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRHL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.054 | 15/46 (NCI-H2030, C-33 A, …) | two highest doses | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | 1.23× | +3.3 | 0.26 | 8/47 (NCI-H2347, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -14.8 | 0e+00 | 39/47 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -14.1 | 1e-42 | 34/46 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -12.0 | 4e-31 | 38/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -8.9 | 6e-17 | 37/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.731×** | -7.1 | 1e-10 | 31/47 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -6.3 | 3e-08 | 31/47 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.1 | 7e-08 | 25/46 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -5.6 | 2e-06 | 28/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 4e-05 | 24/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -4.4 | 6e-04 | 23/45 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.773×** | -4.1 | 0.002 | 20/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.792×** | -3.7 | 0.009 | 19/44 (HS-578T, HCT15, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.788×** | -3.5 | 0.018 | 17/32 (HS-578T, HOP62, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.019 | 20/47 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.683×** | -3.2 | 0.052 | 19/41 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.089 | 16/47 (C-33 A, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.0 | 0 | 8 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -13.5) |
| [[HS-578T (line)]] | alt | 63.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -13.1) |
| [[A-172 (line)]] | wt | 62.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.8) |
| [[A498 (line)]] | wt | 47.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.2) |
| [[A549 (line)]] | wt | 34.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.2) |
| [[H4 (line)]] | wt | 76.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.8) |
| [[J82 (line)]] | alt | 43.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.0) |
| [[SNU-423 (line)]] | alt | 41.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.2) |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.1) |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.3) |
| [[C32 (line)]] | wt | 26.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.3) |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.110× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.300× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -8.8) |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -8.5) |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0801× (z -10.6) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[MIER2]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[YKT6]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[EPN1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | STRING 675 |
| [[ATAD3B]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[DPH7]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[OGG1]] | +0.63 | +0.62 / +0.49 | both halves | 2e-05 |  |
| [[GPSM1]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[TMEM104]] | +0.62 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CHFR]] | +0.61 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CPSF1]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.62 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[CXCL3]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TFAP2A-AS1]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[ARID2]] | -0.58 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MED13]] | -0.58 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[ARL15]] | -0.57 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[CAMK2D]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.56 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[KLRK1-AS1]] | -0.56 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[HOTAIR]] | -0.56 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[PARP8]] | -0.56 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[DLEU1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]] | B | GRHL2 activity lowers AP1M1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.37× higher at baseline in the lines without GRHL2 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[CXCL3]] | B | CXCL3 activity strengthens AP1M1's drug response | lines that do not express CXCL3 (14) vs lines expressing it (33) | the lines without CXCL3 respond 0.41× as strongly (z diff +1.87); strongest at Homoharringtonine 5 µM: 0.85x vs 0.47x (z diff +3.8) | 0.010 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; artifact flags |
| [[HOTAIR]] | B | HOTAIR activity lowers AP1M1's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.31× higher at baseline in the lines without HOTAIR | 0.082 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[TOP2A]] | B | TOP2A activity raises AP1M1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises AP1M1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.39× lower at baseline in the lines without CLTCL1 | 0.012 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-2.8, -26.2); signed map (-50.7, 1.4). **Vector** length 106, 26.3% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +2.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.3 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | -0.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.5 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -14.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit mu 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,197,854-16,245,906 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP47, CLAPM2, mu1A |
| Gene groups (HGNC) | Adaptor related protein complex 1 |
| Reactome | 15 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXS5](https://www.uniprot.org/uniprotkb/Q9BXS5) (AP-1 complex subunit mu-1):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the trans-Golgi network (TGN) and endosomes. The AP complexes mediate the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules.

**Summary**, from NCBI Gene [8907](https://www.ncbi.nlm.nih.gov/gene/8907):

> The protein encoded by this gene is the medium chain of the trans-Golgi network clathrin-associated protein complex AP-1. The other components of this complex are beta-prime-adaptin, gamma-adaptin, and the small chain AP1S1. This complex is located at the Golgi vesicle and links clathrin to receptors in coated vesicles. These vesicles are involved in endocytosis and Golgi processing. Alternatively spliced transcript variants encoding distinct protein isoforms have been found for this gene. …

**Accessions** — [HGNC:13667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13667) · Entrez [8907](https://www.ncbi.nlm.nih.gov/gene/8907) · UniProt [Q9BXS5](https://www.uniprot.org/uniprotkb/Q9BXS5) · Ensembl [ENSG00000072958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072958)

## Data

Gene col 1039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1039); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1039]; `tensor/DDL_lfc|DDL_z.npy` [1039]; `embed/gene_vectors.npy` [1039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1039 or target_col == 1039). Every well: [[AP1M1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1M1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
