---
symbol: "LDHC"
type: "gene"
col: 9358
ensembl_id: "ENSG00000166796"
name: "lactate dehydrogenase C"
location: "11p15.1"
module: 38
arm: "+"
pooled_cpm: 5.18
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# LDHC

*lactate dehydrogenase C* — 11p15.1

> [!summary] In one line
> LDHC encodes the C subunit of lactate dehydrogenase, assembling into the germ-cell-restricted LDH-C4 isozyme that supports sperm energy metabolism.

## What it is

The sixth LDH isozyme was found in human testis in the 1960s and called LDH-X before the subunit got its own gene at 11p15. LDH-C4 is a homotetramer of C subunits catalysing the same pyruvate-lactate interconversion as LDH-A and LDH-B but with a distinct kinetic profile, and normally confined to spermatocytes, spermatids and mature sperm. Loss of C-subunit activity in mouse impairs sperm motility, capacitation and fertilisation, and reduced activity is associated with human male infertility. Because the promoter is silent outside the germline but de-represses in tumours, LDHC is grouped with the cancer-testis antigens, and HLA-A2-restricted peptides from it have been proposed as immunotherapy targets. Reports of a role in tumour motility come from few models.

## What is uncertain

The measurement is the weak point. LDHC shares substantial sequence identity with LDHA and LDHB, both abundant in essentially every cancer line, so a low LDHC count is exactly where read misassignment would show up — importing the behaviour of a major glycolytic gene into this feature. Cancer-testis expression is also strongly line-specific, so an apparent association could be carried by the few lines that de-repress the locus at all.

## References

- Wu et al., 2022, Frontiers in Oncology — review of LDH-C4 in germ-cell metabolism, male infertility and its reclassification as a cancer-testis antigen.
- Naik and Decock, 2023, Frontiers in Oncology — commentary on that review, noting the authors' own earlier identification of HLA-A2-restricted LDHC peptides that elicit cytotoxic T-cell responses.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.46× (z +14.2, q 3e-43, up in 38 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.88, fdr 7e-06), [[TRIM72]] (+0.85, fdr 7e-06), [[GRAMD2A]] (+0.84, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.46×** | +14.2 | 3e-43 | 38/38 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.02×** | +11.7 | 6e-29 | 28/37 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.17×** | +10.8 | 7e-25 | 39/44 (A-172, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.44×** | +8.2 | 4e-14 | 8/14 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +6.8 | 1e-09 | 29/37 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **7.53×** | +6.3 | 4e-08 | 10/13 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +5.6 | 2e-06 | 17/26 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **5.68×** | +5.4 | 5e-06 | 20/30 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +5.1 | 2e-05 | 16/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.19×** | +4.6 | 2e-04 | 21/45 (A498, SW480, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **2.09×** | +4.3 | 7e-04 | 20/47 (HepG2/C3A, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.001 | 17/44 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.013 | 11/46 (A498, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +3.5 | 0.018 | 12/35 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.85×** | +3.4 | 0.022 | 16/43 (A498, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.026 | 12/40 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.80×** | +3.3 | 0.026 | 20/42 (NCI-H1573, C-33 A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.059 | 12/43 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.077 | 12/43 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Infigratinib (drug)]] 0.05 µM |  | 0.549× | -3.4 | 0.36 | 7/42 (MIA PaCa-2, HCT15, …) | inconsistent across doses | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.480× | -3.2 | 0.36 | 9/45 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.501× | -3.0 | 0.45 | 11/45 (COLO 205, NCI-H1573, …) | two highest doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.90 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +11.8) | — |
| [[A-172 (line)]] | wt | 2.97 | 2 | 0 | [[Auranofin (drug)]] 5 µM 70.4× (z +12.1) | — |
| [[A498 (line)]] | wt | 2.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.5) | — |
| [[SW480 (line)]] | alt | 3.49 | 2 | 0 | [[Auranofin (drug)]] 5 µM 15.7× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.3× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 7.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +13.1) | — |
| [[A-427 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD2A]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R36]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FGF18]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[ROPN1L]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LDHC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01291]] | B | LINC01291 activity raises LDHC's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without LINC01291 | 0.043 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[MIA]] | B | MIA activity raises LDHC's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without MIA | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, -16.3); signed map (16.2, 11.3). **Vector** length 92.1, 21.1% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +11.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +5.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | lactate dehydrogenase C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,412,318-18,452,063 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CT32 |
| Gene groups (HGNC) | L-lactate dehydrogenase family |
| Hallmark sets | SPERMATOGENESIS, GLYCOLYSIS, HYPOXIA |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P07864](https://www.uniprot.org/uniprotkb/P07864) (L-lactate dehydrogenase C chain):

> Interconverts simultaneously and stereospecifically pyruvate and L-lactate with concomitant interconversion of NADH and NAD(+). Predominant lactate dehydrogenase isozyme in spermatozoa and spermatogenic cells, where it is required for glycolytic ATP production, sperm motility, capacitation and fertilization (By similarity). Also acts as a regulator of chromatin during late stage of spermatogenesis by acting as a 2-oxoglutarate reductase: translocates into the nucleus and catalyzes the reduction …

**Summary**, from NCBI Gene [3948](https://www.ncbi.nlm.nih.gov/gene/3948):

> Lactate dehydrogenase C catalyzes the conversion of L-lactate and NAD to pyruvate and NADH in the final step of anaerobic glycolysis. LDHC is testis-specific and belongs to the lactate dehydrogenase family. Two transcript variants have been detected which differ in the 5' untranslated region. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6544) · Entrez [3948](https://www.ncbi.nlm.nih.gov/gene/3948) · UniProt [P07864](https://www.uniprot.org/uniprotkb/P07864) · Ensembl [ENSG00000166796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166796)

## Data

Gene col 9358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9358); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9358]; `tensor/DDL_lfc|DDL_z.npy` [9358]; `embed/gene_vectors.npy` [9358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9358 or target_col == 9358). Every well: [[LDHC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/LDHC.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
