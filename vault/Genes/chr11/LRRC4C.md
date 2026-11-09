---
symbol: "LRRC4C"
type: "gene"
col: 7330
ensembl_id: "ENSG00000148948"
name: "leucine rich repeat containing 4C"
location: "11p12"
module: 75
arm: "+"
pooled_cpm: 5.31
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# LRRC4C

*leucine rich repeat containing 4C* — 11p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.84× (z +24.3, q 0e+00, up in 35 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.110×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.0376×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (H4 0.0595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4300HG]] (+0.88, fdr 7e-06), [[DPP6]] (+0.85, fdr 7e-06), [[GALNTL6]] (+0.85, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.84×** | +24.3 | 0e+00 | 35/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.57×** | +23.4 | 0e+00 | 33/40 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +14.0 | 2e-42 | 14/22 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.46×** | +13.5 | 2e-39 | 36/44 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.0 | 6e-26 | 3/9 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +9.6 | 7e-20 | 27/43 (SNU-423, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +8.1 | 5e-14 | 24/46 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.8 | 5e-13 | 6/11 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.5 | 5e-09 | 18/40 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.3 | 2e-08 | 10/47 (A498, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.0 | 1e-07 | 13/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.8 | 4e-07 | 18/41 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.5 | 2e-06 | 13/37 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.2 | 9e-04 | 19/42 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +3.5 | 0.020 | 3/42 (NCI-H460, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7330.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.110×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.0376×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (H4 0.0595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.0 | 0.92 | 14/47 (C32, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.52 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 3.00 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 4.84 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +17.7) | — |
| [[A-172 (line)]] | wt | 2.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.3× (z +17.5) | — |
| [[A498 (line)]] | wt | 7.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +19.2) | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.4× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 3.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +12.4) | — |
| [[A-427 (line)]] | wt | 9.58 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0376× (z -10.7) |
| [[H4 (line)]] | wt | 24.7 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0595× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +12.9) | — |
| [[KATO III (line)]] | alt | 2.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +11.0) | — |
| [[LoVo (line)]] | wt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 | 0 | 1 | — | [[Larotrectinib (drug)]] 5 µM 0.121× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 523 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -12.1) |
| [[PANC-1 (line)]] | alt | 2.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +12.4) | — |
| [[SW480 (line)]] | alt | 2.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.0) | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4300HG]] | +0.88 | +0.82 / +0.86 | both halves | 7e-06 |  |
| [[DPP6]] | +0.85 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.83 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.82 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.82 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[USH2A]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | STRING 605 |
| [[C8orf34]] | +0.82 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[MYO16]] | +0.81 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.81 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.80 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRC4C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRN3]] | C | LRRN3's natural level weakens LRRC4C's drug response | LRRN3's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.33; direction clear | 0.032 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.899). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 28.5); signed map (32.8, 14.2). **Vector** length 65.6, 9.94% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +24.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +23.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p12 — chr11:40,114,203-41,459,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1580, NGL-1 |
| Gene groups (HGNC) | I-set domain containing; Ig-like cell adhesion molecule family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ2](https://www.uniprot.org/uniprotkb/Q9HCJ2) (Leucine-rich repeat-containing protein 4C):

> Synaptic cell-adhesion molecule. During thalamocortical axon development, promotes neurite outgrowth of embryonic thalamic neurons through interaction with NTNG1. At mature excitatory synapses, is phosphorylated by CDKL5 at dendritic spines, which drives stabilization of DLG4/PSD95 at nascent synaptic contacts and promotes dendritic spine formation. Independently of this postsynaptic activity, also induces presynaptic differentiation in contacting axons.

**Summary**, from NCBI Gene [57689](https://www.ncbi.nlm.nih.gov/gene/57689):

> NGL1 is a specific binding partner for netrin G1 (NTNG1; MIM 608818), which is a member of the netrin family of axon guidance molecules (Lin et al., 2003 [PubMed 14595443]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29317) · Entrez [57689](https://www.ncbi.nlm.nih.gov/gene/57689) · UniProt [Q9HCJ2](https://www.uniprot.org/uniprotkb/Q9HCJ2) · Ensembl [ENSG00000148948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148948)

## Data

Gene col 7330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7330); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7330]; `tensor/DDL_lfc|DDL_z.npy` [7330]; `embed/gene_vectors.npy` [7330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7330 or target_col == 7330). Every well: [[LRRC4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
