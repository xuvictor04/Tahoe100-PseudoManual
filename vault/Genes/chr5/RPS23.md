---
symbol: "RPS23"
type: "gene"
col: 11816
ensembl_id: "ENSG00000186468"
name: "ribosomal protein S23"
location: "5q14.2"
module: 131
arm: "+"
pooled_cpm: 280.71
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS23

*ribosomal protein S23* — 5q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +6.5, q 4e-08, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.57× (z +3.8, q 0.023, up in 48 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.40×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -5.7, q 6e-06, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SNU-1 0.214×, SW480 0.336×, RKO 0.326×, LS 180 0.319×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.218×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS11]] (+0.95, fdr 7e-06), [[RPS15]] (+0.94, fdr 7e-06, ⚠ RPS15 in the vector space only through flagged drug-doses), [[RPL32]] (+0.93, fdr 7e-06), [[RPL38]] (+0.93, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.60, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11816.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.40×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +6.5 | 4e-08 | 49/49 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +5.3 | 4e-05 | 43/44 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.02×** | +4.5 | 0.001 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.57×** | +3.8 | 0.023 | 48/48 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.29× | +3.3 | 0.10 | 46/47 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 2.26× | +3.3 | 0.10 | 46/48 (AN3 CA, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | 1.62× | +3.1 | 0.16 | 38/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.1 | 0.16 | 38/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11816.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SNU-1 0.214×, SW480 0.336×, RKO 0.326×, LS 180 0.319×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -5.7 | 6e-06 | 44/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 391 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.5) |
| [[AN3 CA (line)]] | alt | 394 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.1) |
| [[CHP-212 (line)]] | wt | 242 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.7) |
| [[COLO 205 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 358 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 413 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.5) |
| [[RKO (line)]] | wt | 265 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.7) |
| [[SW480 (line)]] | alt | 312 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.7) |
| [[A-172 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 325 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 289 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 203 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 233 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 288 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 190 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 175 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 654 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 369 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 508 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 320 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS11]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS15]] ⚠ | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL32]] | +0.93 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL8]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL38]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS13]] ⚠ | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS25]] | +0.92 | +0.85 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL7A]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL15]] | +0.91 | +0.79 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.90 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.89 | +0.85 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS29]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 869 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.947). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.2, -27.3); signed map (-62.0, -3.3). **Vector** length 92.1, 57.7% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.91 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +1.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.2 — chr5:82,273,320-82,278,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S23, uS12 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 53 pathways, smallest: Protein hydroxylation; SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery |
| Matched by | ensembl_id |

**Function**, from UniProt [P62266](https://www.uniprot.org/uniprotkb/P62266) (Small ribosomal subunit protein uS12):

> Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a …

**Summary**, from NCBI Gene [6228](https://www.ncbi.nlm.nih.gov/gene/6228):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S12P family of ribosomal proteins. It is located in the cytoplasm. The protein shares significant amino acid similarity with S. cerevisiae ribosomal protein S28. As is …

**Accessions** — [HGNC:10410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10410) · Entrez [6228](https://www.ncbi.nlm.nih.gov/gene/6228) · UniProt [P62266](https://www.uniprot.org/uniprotkb/P62266) · Ensembl [ENSG00000186468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186468)

## Data

Gene col 11816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11816); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11816]; `tensor/DDL_lfc|DDL_z.npy` [11816]; `embed/gene_vectors.npy` [11816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11816 or target_col == 11816). Every well: [[RPS23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
