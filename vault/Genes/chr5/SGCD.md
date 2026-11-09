---
symbol: "SGCD"
type: "gene"
col: 9984
ensembl_id: "ENSG00000170624"
name: "sarcoglycan delta"
location: "5q33.2-q33.3"
module: 166
arm: "+"
pooled_cpm: 4.18
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# SGCD

*sarcoglycan delta* — 5q33.2-q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.06× (z +23.1, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.771× (z -3.8, q 0.100, down in 8 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.150×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0955×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.111×; ⚠ cell-cycle shift, explains ~23% of this change); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (HOP62 0.0547×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST8SIA1]] (+0.79, fdr 7e-06), [[CFAP20DC-DT]] (+0.78, fdr 7e-06), [[DCC]] (+0.78, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +23.1 | 0e+00 | 29/32 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.35×** | +16.9 | 0e+00 | 12/14 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.12×** | +15.8 | 0e+00 | 1/4 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +10.3 | 7e-23 | 3/6 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.72×** | +10.1 | 8e-22 | 27/41 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.8 | 1e-20 | 18/33 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.5 | 7e-09 | 12/23 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.7 | 7e-07 | 10/30 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.6 | 2e-06 | 14/35 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 8/45 (A-172, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.3 | 8e-04 | 11/44 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.012 | 5/42 (C32, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.017 | 9/38 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.027 | 5/44 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.4 | 0.027 | 1/4 (A-172) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.095 | 6/39 (A-172, SW1417, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.095 | 2/42 (C32, SK-MEL-2) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9984.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.150×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0955×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.111×; ⚠ cell-cycle shift, explains ~23% of this change); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (HOP62 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.771×** | -3.8 | 0.100 | 8/44 (A-172, HS-578T, …) | top dose only | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.46 | 6/29 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 51.0 | 1 | 1 (1 ⚠) | [[Binimetinib (drug)]] 0.5 µM 4.56× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0955× (z -10.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 44.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.2) |
| [[A-172 (line)]] | wt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.62× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 1.99 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.5 µM 0.0547× (z -8.6) |
| [[LoVo (line)]] | wt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 1.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.65× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +10.4) | — |
| [[A-427 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST8SIA1]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CFAP20DC-DT]] | +0.78 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[DCC]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02208]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.74 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RFTN2]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[BTNL12P]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[COL24A1]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[CNTNAP4]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[ESR1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SGCD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.4, 27.3); signed map (31.7, 14.9). **Vector** length 57.9, 8.19% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +23.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -0.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sarcoglycan delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2-q33.3 — chr5:155,870,344-156,767,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAGD, LGMD2F, CMD1L |
| Gene groups (HGNC) | Sarcoglycans |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92629](https://www.uniprot.org/uniprotkb/Q92629) (Delta-sarcoglycan):

> Component of the sarcoglycan complex, a subcomplex of the dystrophin-glycoprotein complex which forms a link between the F-actin cytoskeleton and the extracellular matrix.

**Summary**, from NCBI Gene [6444](https://www.ncbi.nlm.nih.gov/gene/6444):

> The protein encoded by this gene is one of the four known components of the sarcoglycan complex, which is a subcomplex of the dystrophin-glycoprotein complex (DGC). DGC forms a link between the F-actin cytoskeleton and the extracellular matrix. This protein is expressed most abundantly in skeletal and cardiac muscle. Mutations in this gene have been associated with autosomal recessive limb-girdle muscular dystrophy and dilated cardiomyopathy. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:10807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10807) · Entrez [6444](https://www.ncbi.nlm.nih.gov/gene/6444) · UniProt [Q92629](https://www.uniprot.org/uniprotkb/Q92629) · Ensembl [ENSG00000170624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170624)

## Data

Gene col 9984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9984); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9984]; `tensor/DDL_lfc|DDL_z.npy` [9984]; `embed/gene_vectors.npy` [9984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9984 or target_col == 9984). Every well: [[SGCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
