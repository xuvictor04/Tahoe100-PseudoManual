---
symbol: "CUX2"
type: "gene"
col: 3208
ensembl_id: "ENSG00000111249"
name: "cut like homeobox 2"
location: "12q24.11-q24.12"
module: 140
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# CUX2

*cut like homeobox 2* — 12q24.11-q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.12× (z +22.7, q 0e+00, up in 24 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0416×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0946×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.0867×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.0932×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORCS3]] (+0.71, fdr 1e-05), [[KCNB1]] (+0.68, fdr 7e-06), [[SLC27A6]] (+0.66, fdr 1e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.12×** | +22.7 | 0e+00 | 24/25 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.52×** | +15.9 | 0e+00 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.85×** | +14.5 | 4e-45 | 6/10 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.84×** | +13.4 | 2e-38 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.70×** | +8.1 | 6e-14 | 21/40 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.9 | 4e-10 | 8/27 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +5.9 | 2e-07 | 14/44 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +5.7 | 1e-06 | 11/31 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.2 | 2e-05 | 2/12 (NCI-H460, NCI-H1573) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.0 | 3e-05 | 3/20 (A549, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.8 | 9e-05 | 5/43 (A549, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.5 | 4e-04 | 4/26 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.2 | 0.001 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.2 | 0.001 | 3/5 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +3.9 | 0.004 | 7/43 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.90×** | +3.7 | 0.006 | 7/39 (NCI-H2347, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.007 | 6/30 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0416×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0946×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.0867×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.0932×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.669× | -3.2 | 0.42 | 3/40 (SNU-423, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.42 | 2/44 (BT-474, MIA PaCa-2) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0416× (z -19.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0203× (z -11.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -9.5) |
| [[A549 (line)]] | wt | 3.30 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 12.7× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 8.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.895 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.887 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.967 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORCS3]] | +0.71 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SLC27A6]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MEIOC]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GALNT17]] | +0.65 | +0.46 / +0.72 | both halves | 3e-05 | same gene group |
| [[HPSE2]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 | same gene group |
| [[LINC02006]] | +0.64 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[CDH23]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 | same gene group |
| [[GREB1]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CRLF1]] | +0.61 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[A2ML1-AS1]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[USH2A]] | +0.60 | +0.46 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CUX2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 28.7); signed map (32.3, 12.2). **Vector** length 48.8, 6.78% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +22.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cut like homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11-q24.12 — chr12:111,034,165-111,350,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0293, CDP2; previously CUTL2 |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14529](https://www.uniprot.org/uniprotkb/O14529) (Homeobox protein cut-like 2):

> Transcription factor involved in the control of neuronal proliferation and differentiation in the brain. Regulates dendrite development and branching, dendritic spine formation, and synaptogenesis in cortical layers II-III. Binds to DNA in a sequence-specific manner.

**Summary**, from NCBI Gene [23316](https://www.ncbi.nlm.nih.gov/gene/23316):

> This gene encodes a protein which contains three CUT domains and a homeodomain; both domains are DNA-binding motifs. A similar gene, whose gene product possesses different DNA-binding activities, is located on chromosome on chromosome 7. Two pseudogenes of this gene have been identified on chromosomes 10 and 4. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:19347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19347) · Entrez [23316](https://www.ncbi.nlm.nih.gov/gene/23316) · UniProt [O14529](https://www.uniprot.org/uniprotkb/O14529) · Ensembl [ENSG00000111249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111249)

## Data

Gene col 3208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3208); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3208]; `tensor/DDL_lfc|DDL_z.npy` [3208]; `embed/gene_vectors.npy` [3208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3208 or target_col == 3208). Every well: [[CUX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
