---
symbol: "RPL30"
type: "gene"
col: 7986
ensembl_id: "ENSG00000156482"
name: "ribosomal protein L30"
location: "8q22.2"
module: 43
arm: "+"
pooled_cpm: 252.65
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL30

*ribosomal protein L30* — 8q22.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.81× (z +8.1, q 3e-13, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (COLO 205 5.34×, SW480 4.39×, LoVo 4.48×, A549 4.64×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 3.28×, SW480 3.66×, A-172 3.47×, LoVo 3.47×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.52×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL19]] (+0.94, fdr 7e-06), [[RPL37]] (+0.93, fdr 7e-06, ⚠ RPL37 in the vector space only through flagged drug-doses), [[RPS12]] (+0.92, fdr 7e-06), [[RPS4X]] (+0.91, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (COLO 205 5.34×, SW480 4.39×, LoVo 4.48×, A549 4.64×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 3.28×, SW480 3.66×, A-172 3.47×, LoVo 3.47×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.52×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +8.1 | 3e-13 | 43/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +7.8 | 2e-12 | 49/49 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.08×** | +6.0 | 4e-07 | 48/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +5.6 | 4e-06 | 42/45 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.007 | 40/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.56×** | +3.6 | 0.029 | 39/48 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.54×** | +3.4 | 0.057 | 35/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.32× | +3.2 | 0.11 | 31/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 236 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 259 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 393 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 212 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 401 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[A-427 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 300 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 238 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 350 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 239 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 228 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 220 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 237 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 267 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 311 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 355 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 246 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 504 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 291 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL19]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.91 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP1]] | +0.90 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[NACA]] ⚠ | +0.90 | +0.84 / +0.90 | both halves | 7e-06 | STRING 980; ⚠ in the vector space only through flagged drug-doses |
| [[RPL11]] | +0.89 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.89 | +0.83 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.89 | +0.83 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.936). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.3, -28.8); signed map (-60.1, -5.5). **Vector** length 73.5, 41.9% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.79 to 19); *Translation initiation complex formation* (reactome, mean cos +0.76 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.76 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.1 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,024,851-98,046,469 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L30, eL30 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62888](https://www.uniprot.org/uniprotkb/P62888) (Large ribosomal subunit protein eL30):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6156](https://www.ncbi.nlm.nih.gov/gene/6156):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L30E family of ribosomal proteins. It is located in the cytoplasm. This gene is co-transcribed with the U72 small nucleolar RNA gene, which is located in its fourth intron. …

**Accessions** — [HGNC:10333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10333) · Entrez [6156](https://www.ncbi.nlm.nih.gov/gene/6156) · UniProt [P62888](https://www.uniprot.org/uniprotkb/P62888) · Ensembl [ENSG00000156482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156482)

## Data

Gene col 7986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7986); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7986]; `tensor/DDL_lfc|DDL_z.npy` [7986]; `embed/gene_vectors.npy` [7986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7986 or target_col == 7986). Every well: [[RPL30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
