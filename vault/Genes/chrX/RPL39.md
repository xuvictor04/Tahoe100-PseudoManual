---
symbol: "RPL39"
type: "gene"
col: 12737
ensembl_id: "ENSG00000198918"
name: "ribosomal protein L39"
location: "Xq24"
module: 43
arm: "+"
pooled_cpm: 118.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL39

*ribosomal protein L39* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.33× (z +7.9, q 1e-12, up in 47 of 47 measured lines) ⚠ transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.63× (z +4.6, q 6e-04, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.686× (z -5.0, q 4e-04, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.453×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0]] (+0.90, fdr 7e-06), [[RPL27A]] (+0.87, fdr 7e-06), [[RPS20]] (+0.86, fdr 7e-06); moves opposite to [[THOP1]] (-0.62, fdr 7e-06), [[SLC35A4]] (-0.58, fdr 1e-05), [[PHF19]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.33×** | +7.9 | 1e-12 | 47/47 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +7.4 | 4e-11 | 42/45 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.0 | 7e-10 | 43/44 (A549, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +6.8 | 1e-09 | 47/49 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 6e-04 | 41/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.002 | 42/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +3.8 | 0.011 | 38/48 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.2 | 0.093 | 31/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.2 | 0.093 | 32/45 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 28/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12737.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.453×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -5.0 | 4e-04 | 37/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.86× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 98.3 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.26× (z +9.8) ⚠ transcription drop | — |
| [[KATO III (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.92× (z +9.7) ⚠ transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.91× (z +9.1) ⚠ transcription drop | — |
| [[PANC-1 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.83× (z +8.7) ⚠ transcription drop | — |
| [[SW1417 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.76× (z +8.6) ⚠ transcription drop | — |
| [[SW480 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.7) |
| [[A-172 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 156 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 132 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL27A]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPS20]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RACK1]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; STRING 998 |
| [[RPL30]] ⚠ | +0.80 | +0.69 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL11]] | +0.80 | +0.75 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPS24]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.79 | +0.71 / +0.78 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.79 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL29]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOP1]] | -0.62 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[PHF19]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZC3H7B]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MIS12]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RPL39's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.2, -29.6); signed map (-61.1, -6.1). **Vector** length 85.3, 34.2% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.67 to 19); *Translation initiation complex formation* (reactome, mean cos +0.66 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.66 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.1 | -0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.0 | -0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.7 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,786,504-119,791,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L39, eL39; previously RPL39P42 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62891](https://www.uniprot.org/uniprotkb/P62891) (Large ribosomal subunit protein eL39):

> RNA-binding component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6170](https://www.ncbi.nlm.nih.gov/gene/6170):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the S39E family of ribosomal proteins. It is located in the cytoplasm. In rat, the protein is the smallest, and one of the most basic, proteins of the ribosome. This gene is …

**Accessions** — [HGNC:10350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10350) · Entrez [6170](https://www.ncbi.nlm.nih.gov/gene/6170) · UniProt [P62891](https://www.uniprot.org/uniprotkb/P62891) · Ensembl [ENSG00000198918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198918)

## Data

Gene col 12737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12737); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12737]; `tensor/DDL_lfc|DDL_z.npy` [12737]; `embed/gene_vectors.npy` [12737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12737 or target_col == 12737). Every well: [[RPL39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
