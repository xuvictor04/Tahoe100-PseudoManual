---
symbol: "PEMT"
type: "gene"
col: 5404
ensembl_id: "ENSG00000133027"
name: "phosphatidylethanolamine N-methyltransferase"
location: "17p11.2"
module: 18
arm: "+"
pooled_cpm: 13.8
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PEMT

*phosphatidylethanolamine N-methyltransferase* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +13.2, q 4e-37, up in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.50× (z +4.8, q 2e-04, up in 10 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -18.6, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.67, fdr 7e-06), [[FAM20B]] (+0.66, fdr 7e-06), [[RPIA]] (+0.66, fdr 7e-06); moves opposite to [[IFNAR1]] (-0.62, fdr 1e-05), [[TRMT1L]] (-0.58, fdr 1e-05), [[SGO1-AS1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +13.2 | 4e-37 | 32/39 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.1 | 4e-31 | 15/23 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.9 | 7e-07 | 15/32 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.2 | 2e-05 | 18/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 2e-04 | 10/43 (A-427, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 9/47 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.3 | 0.081 | 13/42 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.081 | 14/47 (SW 900, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.081 | 4/45 (A498, LS 180, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.081 | 3/20 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.081 | 9/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +3.1 | 0.081 | 5/46 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.097 | 5/44 (SHP-77, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -18.6 | 0e+00 | 39/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -10.6 | 5e-24 | 33/46 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.615×** | -8.1 | 1e-13 | 24/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.716×** | -7.9 | 4e-13 | 28/48 (HOP62, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -5.8 | 6e-07 | 22/47 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -5.8 | 6e-07 | 21/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.715×** | -5.6 | 2e-06 | 21/47 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -5.6 | 2e-06 | 23/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -5.5 | 2e-06 | 20/47 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -5.5 | 3e-06 | 18/47 (SW48, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.3 | 7e-06 | 21/48 (A-427, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.730×** | -5.2 | 7e-06 | 22/47 (NCI-H2030, SW48, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.725×** | -5.2 | 1e-05 | 15/46 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -4.9 | 4e-05 | 19/47 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.584×** | -4.7 | 1e-04 | 15/48 (NCI-H2030, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +18.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.5) |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.8) |
| [[RKO (line)]] | wt | 21.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -11.4) |
| [[A-427 (line)]] | wt | 19.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -11.6) |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.0) |
| [[KATO III (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.3) |
| [[SHP-77 (line)]] | alt | 62.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0667× (z -10.8) |
| [[SW48 (line)]] | wt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.3) |
| [[A-172 (line)]] | wt | 8.32 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.138× (z -11.0) |
| [[A498 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.1) |
| [[A549 (line)]] | wt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.2) |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.8) |
| [[H4 (line)]] | wt | 11.7 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0834× (z -9.1) |
| [[J82 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.3) |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -12.1) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.9) |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RPIA]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DDX54]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[WDR5]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MON1A]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[NTAQ1]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[DFFB]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[POLRMT]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TRAP1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.55 | -0.60 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises PEMT's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without NT5M | 0.007 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[DUXAP9]] | B | DUXAP9 activity raises PEMT's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without DUXAP9 | 0.030 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[LINC01237]] | B | LINC01237 activity raises PEMT's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without LINC01237 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.9, -28.8); signed map (-43.0, -16.2). **Vector** length 78.8, 14.9% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -18.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -7.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.4 | -1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylethanolamine N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,505,563-17,591,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEMPT, PEMT2 |
| Gene groups (HGNC) | Membrane-bound methyltransferase family; Small molecule methyltransferases |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBM1](https://www.uniprot.org/uniprotkb/Q9UBM1) (Phosphatidylethanolamine N-methyltransferase):

> Catalyzes the three sequential steps of the methylation pathway for the biosynthesis of phosphatidylcholine, a critical and essential component for membrane structure. Uses S-adenosylmethionine (S-adenosyl-L-methionine, SAM or AdoMet) as the methyl group donor for the methylation of phosphatidylethanolamine (1,2-diacyl-sn-glycero-3-phosphoethanolamine, PE) to phosphatidylmonomethylethanolamine (1,2-diacyl-sn-glycero-3-phospho-N-methylethanolamine, PMME), PMME to phosphatidyldimethylethanolamine …

**Summary**, from NCBI Gene [10400](https://www.ncbi.nlm.nih.gov/gene/10400):

> Phosphatidylcholine (PC) is the most abundant mammalian phospholipid. This gene encodes an enzyme which converts phosphatidylethanolamine to phosphatidylcholine by sequential methylation in the liver. Another distinct synthetic pathway in nucleated cells converts intracellular choline to phosphatidylcholine by a three-step process. The protein isoforms encoded by this gene localize to the endoplasmic reticulum and mitochondria-associated membranes. Alternate splicing of this gene results in …

**Accessions** — [HGNC:8830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8830) · Entrez [10400](https://www.ncbi.nlm.nih.gov/gene/10400) · UniProt [Q9UBM1](https://www.uniprot.org/uniprotkb/Q9UBM1) · Ensembl [ENSG00000133027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133027)

## Data

Gene col 5404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5404); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5404]; `tensor/DDL_lfc|DDL_z.npy` [5404]; `embed/gene_vectors.npy` [5404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5404 or target_col == 5404). Every well: [[PEMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
