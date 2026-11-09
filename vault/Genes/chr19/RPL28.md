---
symbol: "RPL28"
type: "gene"
col: 2920
ensembl_id: "ENSG00000108107"
name: "ribosomal protein L28"
location: "19q13.42"
module: 131
arm: "+"
pooled_cpm: 258.36
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL28

*ribosomal protein L28* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +6.8, q 7e-09, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +4.4, q 0.001, up in 43 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 3.86×, SHP-77 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -4.9, q 4e-04, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.392×, A-427 0.356×, RKO 0.366×, NCI-H2347 0.405×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL32]] (+0.95, fdr 7e-06), [[RPS11]] (+0.95, fdr 7e-06), [[RPS25]] (+0.94, fdr 7e-06); moves opposite to [[DCLRE1A]] (-0.68, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CSTB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 3.86×, SHP-77 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.88×** | +6.8 | 7e-09 | 48/49 (SHP-77, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.35×** | +6.0 | 5e-07 | 43/44 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.91×** | +4.8 | 4e-04 | 47/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.4 | 0.001 | 43/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.90×** | +4.4 | 0.001 | 41/45 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.2 | 0.003 | 41/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.69×** | +3.9 | 0.009 | 46/48 (HT-29, A-172, …) | two highest doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.4 | 0.052 | 1/50 (BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.392×, A-427 0.356×, RKO 0.366×, NCI-H2347 0.405×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -4.9 | 4e-04 | 42/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.5) |
| [[C-33 A (line)]] | alt | 320 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.5) |
| [[H4 (line)]] | wt | 421 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 212 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 279 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.0) |
| [[RKO (line)]] | wt | 288 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.4) |
| [[SHP-77 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 271 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 352 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 234 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 330 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 197 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 304 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 267 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 284 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 398 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 266 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 373 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 248 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL32]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS11]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.94 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL8]] ⚠ | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS10]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPL7A]] | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.68 | -0.66 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTB]] | B | CSTB activity raises RPL28's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CSTB | 0.057 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.953). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.9, -27.2); signed map (-61.6, -3.3). **Vector** length 93.2, 56.6% of its response variance represented; |z| ≥ 3 in 466 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.90 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.91 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.91 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.7 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +2.0 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -7.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.9 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,385,932-55,403,250 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43307, L28, eL28 |
| Gene groups (HGNC) | L ribosomal proteins; MicroRNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46779](https://www.uniprot.org/uniprotkb/P46779) (Large ribosomal subunit protein eL28):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6158](https://www.ncbi.nlm.nih.gov/gene/6158):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L28E family of ribosomal proteins. It is located in the cytoplasm. Variable expression of this gene in colorectal cancers compared to adjacent normal tissues has been …

**Accessions** — [HGNC:10330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10330) · Entrez [6158](https://www.ncbi.nlm.nih.gov/gene/6158) · UniProt [P46779](https://www.uniprot.org/uniprotkb/P46779) · Ensembl [ENSG00000108107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108107)

## Data

Gene col 2920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2920); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2920]; `tensor/DDL_lfc|DDL_z.npy` [2920]; `embed/gene_vectors.npy` [2920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2920 or target_col == 2920). Every well: [[RPL28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
