---
symbol: "RPL27A"
type: "gene"
col: 9306
ensembl_id: "ENSG00000166441"
name: "ribosomal protein L27a"
location: "11p15.4"
module: 43
arm: "+"
pooled_cpm: 237.28
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL27A

*ribosomal protein L27a* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +7.1, q 1e-09, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 5.59×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.23×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 4.13×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.526× (z -7.7, q 8e-12, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.340×, NCI-H2030 0.325×, SNU-1 0.327×, LS 180 0.360×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.250×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS20]] (+0.92, fdr 7e-06), [[RPLP0]] (+0.92, fdr 7e-06), [[RPL12]] (+0.92, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.69, fdr 7e-06), [[DCLRE1A]] (-0.64, fdr 7e-06), [[FAM111A]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EEF1G]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 5.59×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.23×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 4.13×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +7.1 | 1e-09 | 47/49 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +6.3 | 9e-08 | 42/44 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.9 | 5e-07 | 43/45 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.6 | 3e-06 | 47/48 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.340×, NCI-H2030 0.325×, SNU-1 0.327×, LS 180 0.360×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.250×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -7.7 | 8e-12 | 44/48 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -4.5 | 0.002 | 39/48 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 220 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 316 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) |
| [[BT-474 (line)]] | alt | 223 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.9) |
| [[C-33 A (line)]] | alt | 245 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.2) |
| [[HT-29 (line)]] | alt | 402 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -10.2) |
| [[J82 (line)]] | alt | 247 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.8) |
| [[LoVo (line)]] | wt | 475 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 310 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.5) |
| [[LS 180 (line)]] | wt | 306 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 189 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.9) |
| [[SHP-77 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.59× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 285 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.2) |
| [[SW1417 (line)]] | alt | 255 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.7) |
| [[SW480 (line)]] | alt | 313 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.6) |
| [[A-172 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 215 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 205 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 283 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 167 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 228 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 123 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 250 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 278 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS20]] | +0.92 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP0]] | +0.92 | +0.90 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.92 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.89 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.89 | +0.83 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.89 | +0.88 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.89 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.88 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.69 | -0.66 / -0.66 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[FAM111A]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[MIS12]] | -0.64 | -0.62 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF1G]] | C | EEF1G's natural level strengthens RPL27A's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.28; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.3, -29.2); signed map (-61.1, -5.7). **Vector** length 88.9, 47.9% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.76 to 19); *Translation initiation complex formation* (reactome, mean cos +0.74 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.74 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.0 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.7 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.0 | +0.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.0 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L27a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,682,788-8,714,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L27A, uL15 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 39 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; Peptide chain elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46776](https://www.uniprot.org/uniprotkb/P46776) (Large ribosomal subunit protein uL15):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6157](https://www.ncbi.nlm.nih.gov/gene/6157):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L15P family of ribosomal proteins. It is located in the cytoplasm. Variable expression of this gene in colorectal cancers compared to adjacent normal tissues has been …

**Accessions** — [HGNC:10329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10329) · Entrez [6157](https://www.ncbi.nlm.nih.gov/gene/6157) · UniProt [P46776](https://www.uniprot.org/uniprotkb/P46776) · Ensembl [ENSG00000166441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166441)

## Data

Gene col 9306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9306); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9306]; `tensor/DDL_lfc|DDL_z.npy` [9306]; `embed/gene_vectors.npy` [9306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9306 or target_col == 9306). Every well: [[RPL27A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL27A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
